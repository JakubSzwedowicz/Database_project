from pymongo import MongoClient

client = MongoClient("mongodb+srv://mongo:54321@cluster0.9e7ffrw.mongodb.net/?retryWrites=true&w=majority")
db = client["Akademiki"]

utensils_def = {
    "bsonType": "array",
    "items": {
        "bsonType": "object",
        "required": [
            "description",
            "quantity"
        ],
        "properties": {
            "description": {
                "bsonType": "string"
            },
            "quantity": {
                "bsonType": "int"
            }
        }
    }
}

applications_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "title": "User Object Validation",
        "required": [
            "applications",
            "student_id"
        ],
        "properties": {
            "student_id": {
                "bsonType": "objectId"
            },
            "applications": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "required": [
                        "receive_date",
                        "application_type",
                        "application_history"
                    ],
                    "properties": {
                        "receive_date": {
                            "bsonType": "date"
                        },
                        "application_type": {
                            "bsonType": "string",
                            "enum": [
                                "rent",
                                "parking_spot",
                                "utensils"
                            ]
                        },
                        "application_history": {
                            "bsonType": "array",
                            "items": {
                                "bsonType": "object",
                                "required": [
                                    "user_id",
                                    "date_of_change",
                                    "notes",
                                    "status"
                                ],
                                "properties": {
                                    "user_id": {
                                        "bsonType": "objectId"
                                    },
                                    "date_of_change": {
                                        "bsonType": "date"
                                    },
                                    "notes": {
                                        "bsonType": "string"
                                    },
                                    "status": {
                                        "bsonType": "string",
                                        "enum": [
                                            "not sent",
                                            "pending",
                                            "accepted",
                                            "declined"
                                        ]
                                    },
                                    "room_number": {
                                        "bsonType": "int"
                                    },
                                    "parking_spot_number": {
                                        "bsonType": "int"
                                    },
                                    "parking_spot_building_number": {
                                        "bsonType": "string"
                                    },
                                    "utensils": utensils_def
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

buildings_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "title": "Building Object Validation",
        "required": [
            "name",
            "street",
            "building_number",
            "city",
            "postal_code"
        ],
        "properties": {
            "name": {
                "bsonType": "string",
            },
            "street": {
                "bsonType": "string",
            },
            "building_number": {
                "bsonType": "string",
            },
            "city": {
                "bsonType": "string",
            },
            "postal_code": {
                "bsonType": "string",
            },
            "floors": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "required": [
                        "number",
                        "room"
                    ],
                    "properties": {
                        "number": {
                            "bsonType": "int",
                        },
                        "room": {
                            "bsonType": "array",
                            "items": {
                                "bsonType": "object",
                                "required": [
                                    "number",
                                    "occupants"
                                ],
                                "properties": {
                                    "number": {
                                        "bsonType": "int",
                                    },
                                    "occupants": {
                                        "bsonType": "array",
                                        "items": {
                                            "bsonType": "objectId",
                                        }
                                    },
                                    "utensils": utensils_def,
                                }
                            }
                        },
                        "utensils": utensils_def,
                    }
                },
            },
            "parking_spot": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "required": [
                        "number",
                        "owner_id"
                    ],
                    "properties": {
                        "number": {
                            "bsonType": "int",
                        },
                        "owner_id": {
                            "bsonType": "objectId",
                        }
                    },
                },
            }
        }
    }
}

users_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "title": "User Object Validation",
        "required": [
            "first_name",
            "last_name",
            "street",
            "email",
            "phone_number",
            "city",
            "postal_code",
            "user_type"
        ],
        "properties": {
                          "first_name": {
                              "bsonType": "string",
                              "description": "'first_name' must be a string and is required"
                          },
                          "last_name": {
                              "bsonType": "string",
                              "description": "'last_name' must be a string and is required"
                          },
                          "street": {
                              "bsonType": "string",
                              "description": "'street' must be a string and is required"
                          },
                          "email": {
                              "bsonType": "string",
                              "description": "'email' must be a string and is required"
                          },
                          "phone_number": {
                              "bsonType": "string",
                              "description": "'phone_number' must be a string and is required"
                          },
                          "city": {
                              "bsonType": "string",
                              "description": "'city' must be a string and is required"
                          },
                          "postal_code": {
                              "bsonType": "string",
                              "description": "'postal_code' must be a string and is required"
                          },
                          "user_type": {
                              "bsonType": "string",
                              "enum": [
                                  'student',
                                  'employee',
                                  'admin'
                              ], "description": "'user_type' must be a string and is required"
                          },
                          "student_number": {
                              "bsonType": "string",
                              "description": "'student_number' must be a string and is required",
                          },
                          "is_active": {
                              "bsonType": "bool",
                              "description": "'student_status' must be a string and is required"
                          },
                          "payment": {
                              "bsonType": "array",
                              "items": {
                                  "bsonType": "object",
                                  "required": [
                                      "amount",
                                      "payment_date"
                                  ],
                                  "properties": {
                                      "amount": {
                                          "bsonType": "double",
                                          "minimum": 0.0
                                      },
                                      "payment_date": {
                                          "bsonType": "date"
                                      }
                                  }
                              }
                          },
                          "charge": {
                              "bsonType": "array",
                              "items": {
                                  "bsonType": "object",
                                  "required": [
                                      "amount",
                                      "charge_date"
                                  ],
                                  "properties": {
                                      "amount": {
                                          "bsonType": "double",
                                          "minimum": 0.0
                                      },
                                      "charge_date": {
                                          "bsonType": "date"
                                      }
                                  }
                              }
                          },
                          "resident_card": {
                              "bsonType": "array",
                              "items": {
                                  "bsonType": "object",
                                  "required": [
                                      "expire_date",
                                      "is_active"],
                                  "properties": {
                                      "expire_date": {
                                          "bsonType": "date"
                                      },
                                      "is_active": {
                                          "bsonType": "bool",
                                      },
                                      "parking_spot_number": {
                                          "bsonType": "int",
                                      },
                                      "parking_spot_building_number": {
                                          "bsonType": "string",
                                      }
                                  }
                              }
                          },
                          "user_applications": {
                              "bsonType": 'objectId'
                          },
                          "salary": {
                              "bsonType": "double",
                              "minimum": 0.0
                          },
        }
    }
}


if __name__ == '__main__':
    db.create_collection("users_applications", validator=applications_validator)
    db.create_collection("buildings", validator=buildings_validator)
    db.create_collection("users", validator=users_validator)
