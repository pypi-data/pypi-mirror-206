from setuptools import setup

name = "types-SQLAlchemy"
description = "Typing stubs for SQLAlchemy"
long_description = '''
## Typing stubs for SQLAlchemy

This is a PEP 561 type stub package for the `SQLAlchemy` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`SQLAlchemy`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/SQLAlchemy. All fixes for
types and metadata should be contributed there.

The `sqlalchemy-stubs` package is an alternative to this package and also includes a mypy plugin for more precise types.

*Note:* The `SQLAlchemy` package includes type annotations or type stubs
since version 2.0.0. Please uninstall the `types-SQLAlchemy`
package if you use this or a newer version.


See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `e816acffddf9d984bac131224b0eb0f6a3e1c9fc`.
'''.lstrip()

setup(name=name,
      version="1.4.53.38",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/SQLAlchemy.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['sqlalchemy-stubs'],
      package_data={'sqlalchemy-stubs': ['__init__.pyi', 'cimmutabledict.pyi', 'connectors/__init__.pyi', 'connectors/mxodbc.pyi', 'connectors/pyodbc.pyi', 'cprocessors.pyi', 'cresultproxy.pyi', 'databases/__init__.pyi', 'dialects/__init__.pyi', 'dialects/firebird/__init__.pyi', 'dialects/firebird/base.pyi', 'dialects/firebird/fdb.pyi', 'dialects/firebird/kinterbasdb.pyi', 'dialects/mssql/__init__.pyi', 'dialects/mssql/base.pyi', 'dialects/mssql/information_schema.pyi', 'dialects/mssql/json.pyi', 'dialects/mssql/mxodbc.pyi', 'dialects/mssql/provision.pyi', 'dialects/mssql/pymssql.pyi', 'dialects/mssql/pyodbc.pyi', 'dialects/mysql/__init__.pyi', 'dialects/mysql/aiomysql.pyi', 'dialects/mysql/asyncmy.pyi', 'dialects/mysql/base.pyi', 'dialects/mysql/cymysql.pyi', 'dialects/mysql/dml.pyi', 'dialects/mysql/enumerated.pyi', 'dialects/mysql/expression.pyi', 'dialects/mysql/json.pyi', 'dialects/mysql/mariadb.pyi', 'dialects/mysql/mariadbconnector.pyi', 'dialects/mysql/mysqlconnector.pyi', 'dialects/mysql/mysqldb.pyi', 'dialects/mysql/oursql.pyi', 'dialects/mysql/provision.pyi', 'dialects/mysql/pymysql.pyi', 'dialects/mysql/pyodbc.pyi', 'dialects/mysql/reflection.pyi', 'dialects/mysql/reserved_words.pyi', 'dialects/mysql/types.pyi', 'dialects/oracle/__init__.pyi', 'dialects/oracle/base.pyi', 'dialects/oracle/cx_oracle.pyi', 'dialects/oracle/provision.pyi', 'dialects/postgresql/__init__.pyi', 'dialects/postgresql/array.pyi', 'dialects/postgresql/asyncpg.pyi', 'dialects/postgresql/base.pyi', 'dialects/postgresql/dml.pyi', 'dialects/postgresql/ext.pyi', 'dialects/postgresql/hstore.pyi', 'dialects/postgresql/json.pyi', 'dialects/postgresql/pg8000.pyi', 'dialects/postgresql/provision.pyi', 'dialects/postgresql/psycopg2.pyi', 'dialects/postgresql/psycopg2cffi.pyi', 'dialects/postgresql/pygresql.pyi', 'dialects/postgresql/pypostgresql.pyi', 'dialects/postgresql/ranges.pyi', 'dialects/sqlite/__init__.pyi', 'dialects/sqlite/aiosqlite.pyi', 'dialects/sqlite/base.pyi', 'dialects/sqlite/dml.pyi', 'dialects/sqlite/json.pyi', 'dialects/sqlite/provision.pyi', 'dialects/sqlite/pysqlcipher.pyi', 'dialects/sqlite/pysqlite.pyi', 'dialects/sybase/__init__.pyi', 'dialects/sybase/base.pyi', 'dialects/sybase/mxodbc.pyi', 'dialects/sybase/pyodbc.pyi', 'dialects/sybase/pysybase.pyi', 'engine/__init__.pyi', 'engine/base.pyi', 'engine/characteristics.pyi', 'engine/create.pyi', 'engine/cursor.pyi', 'engine/default.pyi', 'engine/events.pyi', 'engine/interfaces.pyi', 'engine/mock.pyi', 'engine/reflection.pyi', 'engine/result.pyi', 'engine/row.pyi', 'engine/strategies.pyi', 'engine/url.pyi', 'engine/util.pyi', 'event/__init__.pyi', 'event/api.pyi', 'event/attr.pyi', 'event/base.pyi', 'event/legacy.pyi', 'event/registry.pyi', 'events.pyi', 'exc.pyi', 'ext/__init__.pyi', 'ext/associationproxy.pyi', 'ext/asyncio/__init__.pyi', 'ext/asyncio/base.pyi', 'ext/asyncio/engine.pyi', 'ext/asyncio/events.pyi', 'ext/asyncio/exc.pyi', 'ext/asyncio/result.pyi', 'ext/asyncio/scoping.pyi', 'ext/asyncio/session.pyi', 'ext/automap.pyi', 'ext/baked.pyi', 'ext/compiler.pyi', 'ext/declarative/__init__.pyi', 'ext/declarative/extensions.pyi', 'ext/horizontal_shard.pyi', 'ext/hybrid.pyi', 'ext/indexable.pyi', 'ext/instrumentation.pyi', 'ext/mutable.pyi', 'ext/orderinglist.pyi', 'ext/serializer.pyi', 'future/__init__.pyi', 'future/engine.pyi', 'future/orm/__init__.pyi', 'inspection.pyi', 'log.pyi', 'orm/__init__.pyi', 'orm/attributes.pyi', 'orm/base.pyi', 'orm/clsregistry.pyi', 'orm/collections.pyi', 'orm/context.pyi', 'orm/decl_api.pyi', 'orm/decl_base.pyi', 'orm/dependency.pyi', 'orm/descriptor_props.pyi', 'orm/dynamic.pyi', 'orm/evaluator.pyi', 'orm/events.pyi', 'orm/exc.pyi', 'orm/identity.pyi', 'orm/instrumentation.pyi', 'orm/interfaces.pyi', 'orm/loading.pyi', 'orm/mapper.pyi', 'orm/path_registry.pyi', 'orm/persistence.pyi', 'orm/properties.pyi', 'orm/query.pyi', 'orm/relationships.pyi', 'orm/scoping.pyi', 'orm/session.pyi', 'orm/state.pyi', 'orm/strategies.pyi', 'orm/strategy_options.pyi', 'orm/sync.pyi', 'orm/unitofwork.pyi', 'orm/util.pyi', 'pool/__init__.pyi', 'pool/base.pyi', 'pool/dbapi_proxy.pyi', 'pool/events.pyi', 'pool/impl.pyi', 'processors.pyi', 'schema.pyi', 'sql/__init__.pyi', 'sql/annotation.pyi', 'sql/base.pyi', 'sql/coercions.pyi', 'sql/compiler.pyi', 'sql/crud.pyi', 'sql/ddl.pyi', 'sql/default_comparator.pyi', 'sql/dml.pyi', 'sql/elements.pyi', 'sql/events.pyi', 'sql/expression.pyi', 'sql/functions.pyi', 'sql/lambdas.pyi', 'sql/naming.pyi', 'sql/operators.pyi', 'sql/roles.pyi', 'sql/schema.pyi', 'sql/selectable.pyi', 'sql/sqltypes.pyi', 'sql/traversals.pyi', 'sql/type_api.pyi', 'sql/util.pyi', 'sql/visitors.pyi', 'testing/__init__.pyi', 'testing/assertions.pyi', 'testing/assertsql.pyi', 'testing/asyncio.pyi', 'testing/config.pyi', 'testing/engines.pyi', 'testing/entities.pyi', 'testing/exclusions.pyi', 'testing/fixtures.pyi', 'testing/mock.pyi', 'testing/pickleable.pyi', 'testing/plugin/__init__.pyi', 'testing/plugin/bootstrap.pyi', 'testing/plugin/plugin_base.pyi', 'testing/plugin/pytestplugin.pyi', 'testing/plugin/reinvent_fixtures_py2k.pyi', 'testing/profiling.pyi', 'testing/provision.pyi', 'testing/requirements.pyi', 'testing/schema.pyi', 'testing/util.pyi', 'testing/warnings.pyi', 'types.pyi', 'util/__init__.pyi', 'util/_collections.pyi', 'util/_compat_py3k.pyi', 'util/_concurrency_py3k.pyi', 'util/_preloaded.pyi', 'util/compat.pyi', 'util/concurrency.pyi', 'util/deprecations.pyi', 'util/langhelpers.pyi', 'util/queue.pyi', 'util/topological.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
