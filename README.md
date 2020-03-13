# インストール方法

```
$ pip install configparser
$ pip install beautifulsoup4
$ pip install unicodecsv
```

# 実行方法

1. sample_config.ini にスクレイピング対象のURLを記載
2. sample_config.ini を config.iniにリネーム
```
$ mv sample_config.ini config.ini
```

3. プログラムの実行

```
$ python scraping.py 
$ ls -lt result.csv 
-rwxr-xr-x 1 vagrant vagrant 6014 Mar 13 23:31 result.csv
```

result.csv にスクレイピング結果が出力されます