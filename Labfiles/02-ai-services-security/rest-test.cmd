curl -X POST "https://mynewmultiservicaccount.cognitiveservices.azure.com//language/:analyze-text?api-version=2023-04-01" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: 7b0ad053ad114164ac8c02b09402c978" --data-ascii "{'analysisInput':{'documents':[{'id':1,'text':'hello'}]}, 'kind': 'LanguageDetection'}"


