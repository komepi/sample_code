a

GET /_cat/indices

PUT /test_index?pretty
{
    "mappings":{
        "properties":{
            "test":{
                "type":"nested",
                "properties":{
                    "test_value":{
                        "type":"keyword"
                    }
                }
            }
        }
        
    }
    
}

DELETE /test_index



GET /test_index/_search
{"query":{"match_all":{}},"size":500}



GET /test_index/_search
{
    "query":{
        "bool":{
            "must":[
                {
                    "nested":{
                        "path":"test",
                        "query":{
                            "bool":{
                                "must":[
                                    {
                                        "exists":{
                                            "field":"test.test_value"
                                        }
                                    }
                                ]
                            }
                        }
                    }
                },
                {"match_all":{}}
            ]
        }
    },
    "aggs":{
        "test_vals":{
            "nested": {
                "path": "test"
            },
            "aggs":{
                "value_list":{
                    "terms":{
                        "field":"test.test_value",
                        "size":5
                    }
                }
            }
        }
    }
}

GET /test_index3/test_type1/12345

PUT /test_index3/test_type1/12345
{"title":["一括2"],"type":["conference paper"],"control_number":"13","_oai":{"id":"oai:weko3.example.org:00000013","sets":["1697690502618"]},"_item_metadata":{"item_1617186331708":{"attribute_name":"Title","attribute_value_mlt":[{"subitem_1551255647225":"一括2","subitem_1551255648112":"ja"}]},"item_1617258105262":{"attribute_name":"Resource Type","attribute_value_mlt":[{"resourcetype":"conference paper","resourceuri":"http://purl.org/coar/resource_type/c_5794"}]},"pubdate":{"attribute_name":"PubDate","attribute_value":"2023-10-19"},"item_title":"一括2","item_type_id":"15","control_number":"13","author_link":[],"_oai":{"id":"oai:weko3.example.org:00000013","sets":["1697690502618"]},"weko_shared_id":-1,"owner":"1","publish_date":"2023-10-19","title":["一括2"],"relation_version_is_last":true,"path":["1697690502618"],"publish_status":"0"},"itemtype":"デフォルトアイテムタイプ（フル）","publish_date":"2023-10-19","author_link":[],"weko_creator_id":"1","weko_shared_id":-1,"path":["1697690502618"],"publish_status":"0","_created":"2023-10-19T00:01:56.181525+00:00","_updated":"2023-10-19T00:01:56.732403+00:00"}

POST /test_index3/test_type1/12345/_update
{"doc":{"feedback_mail_list":[{"email":"test.taro@test.org","author_id":"1"}]}}

HEAD /test_index3/test_type1/12345

PUT /test_index3/test_type1/12345
{"title":["一括2"],"type":["conference paper"],"control_number":"13","_oai":{"id":"oai:weko3.example.org:00000013","sets":["1697690502618"]},"_item_metadata":{"item_1617186331708":{"attribute_name":"Title","attribute_value_mlt":[{"subitem_1551255647225":"一括2","subitem_1551255648112":"ja"}]},"item_1617258105262":{"attribute_name":"Resource Type","attribute_value_mlt":[{"resourcetype":"conference paper","resourceuri":"http://purl.org/coar/resource_type/c_5794"}]},"pubdate":{"attribute_name":"PubDate","attribute_value":"2023-10-19"},"item_title":"一括2","item_type_id":"15","control_number":"13","author_link":[],"_oai":{"id":"oai:weko3.example.org:00000013","sets":["1697690502618"]},"weko_shared_id":-1,"owner":"1","publish_date":"2023-10-19","title":["一括2"],"relation_version_is_last":true,"path":["1697690502618"],"publish_status":"0"},"itemtype":"デフォルトアイテムタイプ（フル）","publish_date":"2023-10-19","author_link":[],"weko_creator_id":"1","weko_shared_id":-1,"path":["1697690502618"],"publish_status":"0","_created":"2023-10-19T00:01:56.181525+00:00","_updated":"2023-10-19T00:01:57.704092+00:00"}