Collecting, processing, indexing, and validating JSON log data using Filebeat, Logstash, and Elasticsearch.


## 1. Run Logstash

Start the Logstash service to listen for incoming data on port `5044`:

```bash
logstash -f ./logstash.conf --path.settings ./logstash_config
```


## 2. Run Filebeat

Launch Filebeat to collect data from JSON files and forward it to Logstash for processing:

```bash
sudo filebeat -e -c ./filebeat.yml --path.data ./filebeat-data --path.logs ./filebeat-logs
```

## 3. Verify Indexed Data in Elasticsearch

Once all the data is indexed, you can verify the indices using the `curl` command:

```bash
curl -u elastic:Gf7sHupiGO0_8kqBpZ5c -k https://localhost:9200/_cat/indices?v
```


## 4. Change Index Health from Yellow to Green

Since the Elasticsearch cluster currently has only one node, set the number of replicas to `0` to turn the index health from **yellow** to **green**:

```bash
curl -u elastic:<your-password> -XPUT -k "https://localhost:9200/software-logs-*/_settings" -H 'Content-Type: application/json' -d'
{
  "index": {
    "number_of_replicas": 0
  }
}'
```


## 5. Archive Raw Data

Use the `archive.sh` script to compress and store the unprocessed raw files in the `/Archive/Data` directory:

```bash
./archive.sh
```
