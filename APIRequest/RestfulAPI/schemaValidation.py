import requests
import jsonschema

# Define your JSON schema
#https://www.liquid-technologies.com/online-json-to-schema-converter
schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "array",
  "items": [
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "slug": {
          "type": "string"
        },
        "created_at": {
          "type": "null"
        },
        "updated_at": {
          "type": "string"
        },
        "subcategories": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "string"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            }
          ]
        }
      },
      "required": [
        "id",
        "name",
        "slug",
        "created_at",
        "updated_at",
        "subcategories"
      ]
    },
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "slug": {
          "type": "string"
        },
        "created_at": {
          "type": "null"
        },
        "updated_at": {
          "type": "string"
        },
        "subcategories": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            }
          ]
        }
      },
      "required": [
        "id",
        "name",
        "slug",
        "created_at",
        "updated_at",
        "subcategories"
      ]
    },
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "slug": {
          "type": "string"
        },
        "created_at": {
          "type": "null"
        },
        "updated_at": {
          "type": "string"
        },
        "subcategories": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            }
          ]
        }
      },
      "required": [
        "id",
        "name",
        "slug",
        "created_at",
        "updated_at",
        "subcategories"
      ]
    },
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "slug": {
          "type": "string"
        },
        "created_at": {
          "type": "null"
        },
        "updated_at": {
          "type": "string"
        },
        "subcategories": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            }
          ]
        }
      },
      "required": [
        "id",
        "name",
        "slug",
        "created_at",
        "updated_at",
        "subcategories"
      ]
    },
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "slug": {
          "type": "string"
        },
        "created_at": {
          "type": "null"
        },
        "updated_at": {
          "type": "null"
        },
        "subcategories": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            }
          ]
        }
      },
      "required": [
        "id",
        "name",
        "slug",
        "created_at",
        "updated_at",
        "subcategories"
      ]
    },
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "slug": {
          "type": "string"
        },
        "created_at": {
          "type": "null"
        },
        "updated_at": {
          "type": "string"
        },
        "subcategories": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            },
            {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "category_id": {
                  "type": "string"
                },
                "image": {
                  "type": "null"
                },
                "created_at": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "category_id",
                "image",
                "created_at",
                "updated_at"
              ]
            }
          ]
        }
      },
      "required": [
        "id",
        "name",
        "slug",
        "created_at",
        "updated_at",
        "subcategories"
      ]
    },
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "slug": {
          "type": "null"
        },
        "created_at": {
          "type": "string"
        },
        "updated_at": {
          "type": "string"
        },
        "subcategories": {
          "type": "array",
          "items": {}
        }
      },
      "required": [
        "id",
        "name",
        "slug",
        "created_at",
        "updated_at",
        "subcategories"
      ]
    },
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "slug": {
          "type": "null"
        },
        "created_at": {
          "type": "string"
        },
        "updated_at": {
          "type": "string"
        },
        "subcategories": {
          "type": "array",
          "items": {}
        }
      },
      "required": [
        "id",
        "name",
        "slug",
        "created_at",
        "updated_at",
        "subcategories"
      ]
    },
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "slug": {
          "type": "null"
        },
        "created_at": {
          "type": "string"
        },
        "updated_at": {
          "type": "string"
        },
        "subcategories": {
          "type": "array",
          "items": {}
        }
      },
      "required": [
        "id",
        "name",
        "slug",
        "created_at",
        "updated_at",
        "subcategories"
      ]
    }
  ]
}


def validate_json_response(url):
    try:
        # Send GET request
        response = requests.get(url)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Retrieve JSON response content
            json_response = response.json()

            # Validate JSON response against schema
            jsonschema.validate(json_response, schema)

            print("JSON response is valid against the schema.")
        else:
            print("Error: Failed to retrieve JSON content. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    except jsonschema.ValidationError as ve:
        print("JSON response does not match the schema:", ve)


# Example usage
url = "https://royalfoodgallery.com/api/categories"
validate_json_response(url)
