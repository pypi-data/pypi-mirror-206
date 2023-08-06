# dfdb
Pandas-like interface for manipulating SQL databases

## Install
`pip install dfdb`

## Overview
This package is a lightweight wrapper around SQLalchemy. As such, it can be used with a variety of database backends, although as of now the package has only been tested with SQLite.

The `dfdb.Database` class provides a dict-like interface of manipulating tables in a SQL database. For example, if we create a `Database` object like

```db = dfdb.Database(filename='data.db', drivername='sqlite')```

Then we can perform operations on a table called `df` in `data.db` by calling, for example

```db['df'].groupby('col1').agg(mean=('col2', 'mean')).fetch()```

`db['df']` is a `dfdb.DataFrame` object that behaves almost identically as a `pandas.DataFrame`. The only difference is that you need to call `.fetch()`, which establishes a connection to the database and performs the corresponding SQL query.

Adding rows to the table is as simple as

```db['df'].append({'col1': 1, 'col2': 2})```

More detailed documentation to follow in the future.
