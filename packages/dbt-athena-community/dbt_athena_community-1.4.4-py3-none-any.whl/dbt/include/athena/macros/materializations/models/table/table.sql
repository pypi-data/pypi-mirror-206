{% materialization table, adapter='athena' -%}
  {%- set identifier = model['alias'] -%}

  {%- set lf_tags = config.get('lf_tags', default=none) -%}
  {%- set lf_tags_columns = config.get('lf_tags_columns', default=none) -%}
  {%- set table_type = config.get('table_type', default='hive') | lower -%}
  {%- set old_relation = adapter.get_relation(database=database, schema=schema, identifier=identifier) -%}
  {%- set target_relation = api.Relation.create(identifier=identifier,
                                                schema=schema,
                                                database=database,
                                                type='table') -%}

  {{ run_hooks(pre_hooks) }}

  {%- if old_relation is none or table_type != 'iceberg' -%}
    {%- if old_relation is not none -%}
      {{ drop_relation(old_relation) }}
    {%- endif -%}

    {%- call statement('main') -%}
      {{ create_table_as(False, target_relation, sql) }}
    {%- endcall %}

    {%- if table_type != 'iceberg' -%}
      {{ set_table_classification(target_relation) }}
    {%- endif -%}
  {%- else -%}
    {%- set tmp_relation = api.Relation.create(identifier=target_relation.identifier ~ '__ha',
                                               schema=schema,
                                               database=database,
                                               s3_path_table_part=target_relation.identifier,
                                               type='table') -%}
    {%- if tmp_relation is not none -%}
      {%- do drop_relation(tmp_relation) -%}
    {%- endif -%}

    {%- set old_relation_bkp = make_temp_relation(old_relation, '__bkp') -%}
    -- If we have this, it means that at least the first renaming occurred but there was an issue
    -- afterwards, therefore we are in weird state. The easiest and cleanest should be to remove
    -- the backup relation. It won't have an impact because since we are in the else condition, that
    -- means that old relation exists therefore no downtime yet.
    {%- if old_relation_bkp is not none -%}
      {%- do drop_relation(old_relation_bkp) -%}
    {%- endif -%}

    {%- call statement('main') -%}
      {{ create_table_as(False, tmp_relation, sql) }}
    {%- endcall -%}

    {{ rename_relation(old_relation, old_relation_bkp) }}
    {{ rename_relation(tmp_relation, target_relation) }}

    {{ drop_relation(old_relation_bkp) }}
  {%- endif -%}

  {{ run_hooks(post_hooks) }}

  {% if lf_tags is not none or lf_tags_columns is not none %}
    {{ adapter.add_lf_tags(target_relation.schema, identifier, lf_tags, lf_tags_columns) }}
  {% endif %}

  {% do persist_docs(target_relation, model) %}

  {{ return({'relations': [target_relation]}) }}

{% endmaterialization %}
