

GET /_cat/indices

GET /test_index/_search
{"query":{"match_all":{}}}


PUT /test_search_after?pretty
{
    "mappings":{
        "properties":{
            "title":{
                "type":"keyword"
            },
            "control_number": {
                "type": "keyword"
            },
            "inin":{
                "type":"keyword"
            }
        }
    }
}


POST _bulk
curl -X POST "localhost:9200/_bulk?pretty" -H 'Content-Type: application/json' -d'
{ "index" : { "_index" : "test_search_after", "_id" : "1" } }
{ "title" : "a" ,"control_number": "1","inin":"1"}
{ "index" : { "_index" : "test_search_after", "_id" : "2" } }
{ "title" : "g" ,"control_number": "2","inin":"2"}
{ "index" : { "_index" : "test_search_after", "_id" : "3" } }
{ "title" : "c" ,"control_number": "3"}
{ "index" : { "_index" : "test_search_after", "_id" : "4" } }
{ "title" : "d" ,"control_number": "4","inin":"4"}
{ "index" : { "_index" : "test_search_after", "_id" : "5" } }
{ "title" : "h" ,"control_number": "5"}
{ "index" : { "_index" : "test_search_after", "_id" : "6" } }
{ "title" : "e" ,"control_number": "6"}
{ "index" : { "_index" : "test_search_after", "_id" : "7" } }
{ "title" : "b" ,"control_number": "7","inin":"7"}
{ "index" : { "_index" : "test_search_after", "_id" : "8" } }
{ "title" : "f" ,"control_number": "8"}
'

GET /test_search_after/_search
{"query":{"match_all":{}}}

GET /test_search_after/_doc/2

GET /test_search_after/_mapping

POST /test_search_after/_doc/2/_update
{"doc":{"title":"g","inin":"2"}}

POST /test_search_after/_doc/2
{"title":"g","control_number":"2","inin":"2"}

POST _bulk

curl -X POST "localhost:9200/_bulk?pretty" -H 'Content-Type: application/json' -d'
{ "update" : {"_id" : "2", "_index" : "test_search_after","retry_on_conflict" : 3} }
{ "doc" : {"title":"g_"} }
{ "update" : {"_id" : "2", "_index" : "test_search_after","retry_on_conflict" : 3} }
{ "script":{"source":"if(ctx._source.inin=='2'){ctx._source.test=21}" ,"lang": "painless"}}
'


POST /test_search_after/_doc/2/_update
{
    "script":{
        "source":"if(ctx._source.inin=='2'){ctx._source.test=1}"
    }
}

GET /test_search_after/_search
{
    "query":{"match_all":{}},
    "sort": [
        {"inin": {"order": "asc"}},
        {"control_number":{"order":"asc"}}
    ]
    
}

GET /test_search_after/_search
{
    "query":{"match_all":{}},
    "sort": [{"inin": {"order": "asc"}},{"control_number": {"order": "asc"}}],
    "size":3,
    "search_after":[null,"5"]
}

GET /test_search_after/_search
{
    "query":{"match_all":{}},
    "sort": [{"inin": {"order": "asc"}}]

}

a,b,c,d,e,f,g,h
1,7,3,4,6,8,2,5

GET /test_search_after/_search
{
    "query":{"match_all":{}},
    "sort": [{"title": {"order": "asc"}}],
    "size":3,
    "search_after":["e"]
}


PUT /test_search_after/_settings
{
    "index": {
        "max_result_window": "10000" 
    }
}

GET /test_search_after/_search
{
    "query":{"match_all":{}},
    "size":3,
    "from":2
}
DELETE /test_search_after


PUT /test_sort?pretty
{
    "mappings":{
        "properties":{
            "title":{
                "type":"keyword"
            },
            "control_number": {
                "type": "keyword"
            }
        }
    }
}


POST _bulk
curl -X POST "localhost:9200/_bulk?pretty" -H 'Content-Type: application/json' -d'
{ "index" : { "_index" : "test_sort", "_id" : "1" } }
{ "title" : "a" ,"control_number": "1"}
{ "index" : { "_index" : "test_sort", "_id" : "2" } }
{ "title" : "g" ,"control_number": "2"}
{ "index" : { "_index" : "test_sort", "_id" : "3" } }
{ "title" : "c" ,"control_number": "3"}
{ "index" : { "_index" : "test_sort", "_id" : "10" } }
{ "title" : "d" ,"control_number": "10"}
{ "index" : { "_index" : "test_sort", "_id" : "20" } }
{ "title" : "h" ,"control_number": "20"}
'

GET /test_sort/_search
{"query":{"match_all":{}}}

GET /test_sort/_search
{
    "query":{"match_all":{}},
    "sort":[{"control_number": {"order": "asc"}}]
}

POST /test_ttt/_doc/1111
{"_item_metadata" : {"owner" : "6","item_files" : {"attribute_name" : "ファイル情報","attribute_type" : "file","attribute_value_mlt" : [{"accessrole" : "open_login","displaytype" : "detail","licensetype" : "license_11","filename" : "2010-4Yamamichi.pdf","format" : "application/pdf","mimetype" : "application/pdf","filesize" : [{"value" : "1.7 MB"}],"version_id" : "cee2a6b5-c3ec-4e0d-8816-70cf185fca08","url" : {"url" : "https://ir.soken.ac.jp/record/5852.1/files/2010-4Yamamichi.pdf"}}]},"item_type_id" : "11","item_resource_type" : {"attribute_name" : "資源タイプ","attribute_value_mlt" : [{"resourceuri" : "http://purl.org/coar/resource_type/c_1843","resourcetype" : "other"}]},"title" : ["日本の保全生態学研究における現在の傾向と今後の課題"],"item_11_description_6" : {"attribute_name" : "内容記述","attribute_value_mlt" : [{"subitem_description_type" : "Other","subitem_description" : "先導科学研究科生命共生体進化学専攻　学籍番号20072356 担当教員 長谷川　眞理子"}]},"author_link" : ["10614"],"item_language" : {"attribute_name" : "言語","attribute_value_mlt" : [{"subitem_language" : "jpn"}]},"path" : ["512"],"item_titles" : {"attribute_name" : "タイトル","attribute_value_mlt" : [{"subitem_title" : "日本の保全生態学研究における現在の傾向と今後の課題"},{"subitem_title" : "Current trends and future problems of conservation ecology researches in Japan","subitem_title_language" : "en"}]},"_oai" : {"sets" : ["512"],"id" : "oai:ir.soken.ac.jp:00005852.1"},"item_creator" : {"attribute_name" : "著者","attribute_type" : "creator","attribute_value_mlt" : [{"creatorNames" : [{"creatorName" : "山道, 真人"},{"creatorName" : "ヤマミチ, マサト","creatorNameLang" : "ja-Kana"}],"nameIdentifiers" : [{"nameIdentifierScheme" : "WEKO","nameIdentifier" : "10614"}]}]},"weko_shared_id" : 6,"relation_version_is_last" : true,"control_number" : "5852.1","item_title" : "日本の保全生態学研究における現在の傾向と今後の課題","publish_date" : "2018-10-29","publish_status" : "0","pubdate" : {"attribute_name" : "公開日","attribute_value" : "2018-10-29"}},"description" : [{"descriptionType" : "Other","value" : "先導科学研究科生命共生体進化学専攻　学籍番号20072356 担当教員 長谷川　眞理子"}],"language" : ["jpn"],"title" : ["日本の保全生態学研究における現在の傾向と今後の課題","Current trends and future problems of conservation ecology researches in Japan"],"type" : ["other"],"content" : [{"accessrole" : "open_no","displaytype" : "detail","licensetype" : "license_11","filename" : "2010-4Yamamichi.pdf","attachment" : { },"format" : "application/pdf","mimetype" : "application/pdf","filesize" : [{"value" : "1.7 MB"}],"version_id" : "378d5d04-d6e6-4614-92ef-2a4a2db84e6b","url" : {"label" : "2010-4Yamamichi.pdf","url" : "https://ir.soken.ac.jp/record/5852.1/files/2010-4Yamamichi.pdf"}}],"author_link" : ["10614"],"path" : ["512"],"file" : {"date" : [ ],"extent" : ["1.7 MB"],"mimeType" : ["application/pdf"],"URI" : [{"value" : "https://ir.soken.ac.jp/record/5852.1/files/2010-4Yamamichi.pdf"}],"version" : [ ]},"control_number" : "5852.1","weko_shared_id" : 6,"relation_version_is_last" : false,"publish_status" : "0","creator" : {"affiliation" : {"affiliationName" : [ ],"nameIdentifier" : [ ]},"givenName" : [ ],"familyName" : [ ],"creatorName" : ["山道, 真人","ヤマミチ, マサト"],"creatorAlternative" : [ ],"nameIdentifier" : ["10614"]},"weko_creator_id" : "6","_updated" : "2023-11-07T09:40:22.181207+00:00","itemtype" : "その他 / Others_04","_oai" : {"sets" : ["512"],"id" : "oai:ir.soken.ac.jp:00005852.1"},"_created" : "2023-06-20T14:35:05.383519+00:00","publish_date" : "2018-10-29"}

GET /test_ttt/_doc/1111

POST /test_ttt/_doc/1111/_update
{
    "script":{
        "source":"for (int i=0; i< ctx._source.content.size(); i++) {if([].contains(ctx._source.content[i].filename)){ctx._source.content[i].accessrole='no_open'}}"
    }
}