# Introduction

Trivia API is used to get questions/answers of a certain category for the Trivia game.

# Getting Started 

* The base URL for all requests is `http://localhost:5000`
* Trivia requires no authentication either by API key or username/password

# Errors

The following table lists some of the error codes that you may receive. The response may also include an `additional_information` string to provide additional information that may be helpful to the user. For example, If no questions are found for the GET request to `/api/questions`, The response will be 

```json
{
    "success": False, 
    "error": 404,
    "message": "Not Found",
    "additional_information": "There are no questions"
}
```

| Status Code | Response | Example JSON | Additional Notes
|---|---|---|---|
| 400 | Bad Request | `{"success": False, "error": 400,"message": "Bad Request"}` | The request was not formatted according to what the server can parse. Check your syntax. |
| 404 | Not Found | `{"success": False, "error": 404,"message": "Not Found"}` | The resource requested was not found on the server. This can be an invalid URL or accessing a book that's not in the database. |
| 405 | Method Not allowed | `{"success": False, "error": 405,"message": "Method Not Allowed"}` | The HTTP method was not allowed for the endpoint. Check your HTTP Method against the documentation for the endpoint and ensure that it's accepted
| 422 | Unprocessable | `{"success": False, "error": 422,"message": "Cannot process"}` | The server cannot process the data that it was given. Check the documentation to make sure that your request has the correct data types. |
| 500 | Internal Server Error | `{"success": False, "error": 500,"message": Internal Server Error"}` | The server is unable to process the request due to a bug on our end. Send a bug report support@localhost.com complete with the exact steps to replicate the bug. |

# Resources

This section is a breakdown of all the endpoints used, grouped by the particular resource

* [Categories](#categories)
    * [GetCategories](#get-categories)
* [Questions](#questions)
    * [GetQuestions](#get-categories)
    * [GetQuestionsOfCategory](#get-questions-of-category)
    * [CreateQuestion](#create-question)
    * [DeleteQuestions](#delete-questions)
    * [SearchQuestions](#search-questions)
* [Quizzes](#quizzes)
    * [PostQuiz](#quizzes)

## <a name="categories">Categories</a>

### <a name='get-categories'>GetCategories</a>

#### Purpose

Get all categories. Limited to 10 categories returned per page request

**Relative URL**: `/api/categories`

**Full URL**: `http://localhost/api/categories`

**HTTP Method**: GET

#### Optional HTTP Parameters

*page* - The expected data for this param is an (integer) number and a 422 error is returned if the data cannot be parsed as a number. Because we're returning ten 10 per page, using different page numbers will return different items. If a page number entered that exceeds the list of pages, a 404 error is returned.

#### Request Format

No Request Body is sent.

#### Response Format

```js
{
    'success': True,
    'categories': [
        {
            'id': int,
            'type': str
        }
    ],
    'total_categories': int
}
```

#### Request Example

No Request Body is sent.

#### Response Example

```js
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }
  ], 
  "success": true, 
  "total_categories": 6
}
```

#### Example CUrl request

```bash
curl -X GET http://localhost:5000/api/categories   
```

## <a name="questions">Questions</a>

### <a name='get-questions'>GetQuestions</a>

#### Purpose

**Relative URL**: `/api/questions`

**Full URL**: `http://localhost:5000/api/questions`

**HTTP Method**: GET

#### Optional HTTP Parameters

*page* - The expected data for this param is an (integer) number and a 422 error is returned if the data cannot be parsed as a number. Because we're returning ten 10 per page, using different page numbers will return different items. If a page number entered that exceeds the list of pages, a 404 error is returned.

#### Request Format

No Request Body is sent.

#### Response Format

```js
{
    'success': True,
    'questions': [
        {
            'id': int,
            'question': str,
            'answer': str,
            'category': int,
            'difficulty': int
        }
    ],
    'total_questions': int
}
```

#### Request Example

No Request Body is sent.

#### Response Example

```js
{
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "success": true, 
  "total_questions": 22
}
```

#### Example CUrl request

```bash
curl -X GET http://localhost:5000/api/questions      
```

### <a name='get-questions-of-category'>GetQuestionsOfCategory</a>

#### Purpose

Get only the questions of a certain category.

**Relative URL**: `/api/categories/<category_id>/questions` where `category_id` is the integer category number.

**Full URL**: `http://localhost:5000/api/categories/<category_id>/questions` where `category_id` is the integer category number.

**HTTP Method**: GET

#### Optional HTTP Parameters

N/A

#### Request Format

No Request Body is sent.

#### Response Format

```js
{
  "current_category": int, 
  "success": bool, 
  "total_questions": int
}
```

#### Request Example

No Request Body is sent.

#### Response Example

```js
{
  "current_category": 3, 
  "success": true, 
  "total_questions": 3
}
```

#### Example CUrl request

```bash
curl -X GET http://localhost:5000/api/categories/3/questions  
```

### <a name='create-question'>CreateQuestion</a>

#### Purpose

Create a new question.

**Relative URL**: `/api/questions`

**Full URL**: `http://localhost:5000/api/questions

**HTTP Method**: POST

#### Optional HTTP Parameters

N/A

#### Request Format

```js
{
    'question': str,
    'answer': str,
    'difficulty': int,
    'category': int
}
```

#### Response Format

```js
{
    'success': bool,
    'question_id': int
}
```

#### Request Example

```js
{
    'question': 'What is the real name of rapper Eminem?',
    'answer': 'Marshal Mathers',
    'difficulty': 4,
    'category': 5
}
```

#### Response Example

```js
{
  "question_id": 27, 
  "success": true
}
```

#### Example CUrl request

```bash
curl -X POST -d '{"question": "What is the real name of rapper Eminem?","answer": "Marshal Mathers","difficulty": 4,"category": 5}' -H 'Content-Type: application/json' http://localhost:5000/api/questions
```

### <a name='delete-questions'>DeleteQuestions</a>

#### Purpose

Delete a question.

**Relative URL**: `/api/questions/<question_id>` where `question_id` is the id of a question that you can find in [GetQuestions](#get-questions)

**Full URL**: `http://localhost:5000/api/questions/<question_id>` where `question_id` is the id of a question that you can find in [GetQuestions](#get-questions)

**HTTP Method**: DELETE

#### Optional HTTP Parameters

N/A

#### Request Format

No Request Body is sent.

#### Response Format

```js
{
    "success": True,
    "message": "Question successfully deleted",
    "question_id": question_id 
}
```

#### Request Example

No Request Body is sent.

#### Response Example

```js
{
  "message": "Question successfully deleted", 
  "question_id": 27, 
  "success": true
}
```

#### Example CUrl request

```bash
curl -X DELETE http://localhost:5000/api/questions/27      
```

### <a name='search-questions'>SearchQuestions</a>

#### Purpose

Search Questions using a string search term.

**Relative URL**: `/api/search/questions/<search_term>` where search term is a string to search for matching questions.

**Full URL**: `http://localhost:5000/api/search/questions/<search_term>` where search term is a string to search for matching questions.

**HTTP Method**: POST

#### Optional HTTP Parameters

N/A

#### Request Format

No Request Body is sent.

#### Response Format

```js
{
  "questions": [
    {
      "answer": str, 
      "category": int, 
      "difficulty": int, 
      "question": str, 
      "question_id": int
    }
  ], 
  "success": bool
}
```

#### Request Example

No Request Body is sent.

#### Response Example

```js
{
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?", 
      "question_id": 2
    }
  ], 
  "success": true
}
```

#### Example CUrl request

```bash
curl -X POST http://localhost:5000/api/search/questions/Tom    
```

## <a name="quizzes">Quizzes</a>

### <a name='post-quiz'>PostQuiz</a>

#### Purpose

This will give the next question of the trivia game. You can either enter a question id if searching for a new question or not enter any question id, which will start the game with the chosen category.

**Relative URL** `/quizzes`

**Full URL** `http://localhost:5000/quizzes`

**HTTP Method** POST

#### Optional HTTP Parameters

N/A

#### Request Format

```js
{
    "quiz_category": {
      "Type": str,
      "id": int
    }
    "previous_questions": [
      int
    ]
}
```

#### Response Format

```js
{
  "next_question": {
    "answer": str, 
    "category": int, 
    "difficulty": int, 
    "id": int, 
    "question": str
  }, 
  "success": bool
}
```

#### Request Example

```js
{
    "category": {
      "type": "Art",
      "id": 2
    }, 
    "previous_question": []
}
```

#### Response Example

```js
{
  "next_question": {
    "answer": "One", 
    "category": 2, 
    "difficulty": 4, 
    "id": 18, 
    "question": "How many paintings did Van Gogh sell in his lifetime?"
  }, 
  "success": true
}
```

#### Example CUrl request

```bash
curl -X POST -H 'Content-Type: application/json' -d '{"quiz_category": {"type": "Art", "id":2}, "previous_question": [2]}' http://localhost:5000/quizzes
```