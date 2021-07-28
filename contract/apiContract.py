# This file contains the contract of the API
getApi={
    "$schema": "http://json-schema.org/draft-04/schema",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "required": [
        "Search",
        "totalResults",
        "Response"
    ],
    "properties": {
        "Search": {
            "type": "array",
            "title": "The Search schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "items": {
                "anyOf": [
                    {
                        "type": "object",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "required": [
                            "Title",
                            "Year",
                            "imdbID",
                            "Type",
                            "Poster"
                        ],
                        "properties": {
                            "Title": {
                                "type": "string",
                                "title": "The Title schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": ""
                            },
                            "Year": {
                                "type": "string",
                                "title": "The Year schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": ""
                            },
                            "imdbID": {
                                "type": "string",
                                "title": "The imdbID schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": ""
                            },
                            "Type": {
                                "type": "string",
                                "title": "The Type schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": ""
                            },
                            "Poster": {
                                "type": "string",
                                "title": "The Poster schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": ""
                            }
                        }
                    }
                ]
            }
        },
        "totalResults": {
            "type": "string",
            "title": "The totalResults schema",
            "description": "An explanation about the purpose of this instance.",
            "default": ""
        },
        "Response": {
            "type": "string",
            "title": "The Response schema",
            "description": "An explanation about the purpose of this instance.",
            "default": ""
        }
    }
}