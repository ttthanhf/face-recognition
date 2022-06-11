
**Api:**
To verify face: 
>localhost:5000/api_v2 (Method: POST, Json: {path: "your path"})
>> => Output {
    status,
    name,
    execute_time,
}

To create new face: 
>localhost:5000/api_v2/create (Method: POST, Json: {path: "your path", name: "your name"})
>> => Output {
    status
    execute_time
}

To scan face: 
>localhost:5000/api_v2/scan (Method: GET)
>> => Output {
    add
    exist
    total
    execute_time
}

To get list: 
>localhost:5000/api_v2/list (Method: GET)
>> => Output {
    *json list*
}

To rename face: 
>localhost:5000/api_v2/rename (Method: POST, Json: {oldname: "your oldname", newname: "your newname"})
>> => Output {
    status
    execute_time
}

To delete face: 
>localhost:5000/api_v2/delete (Method: POST, Json: {name: "your name"})
>> => Output {
    status
    execute_time
}

*Example in folder webapp (it using fetch or axios)

*You can using Postman ! (set body to raw and using method and send it with json)
>ex: 
{
    "name": "Baka"
}

! You need to scan face before create new face !
! You can use test.py if you know :) !

if you have any problem, you can contact to me ! :)


