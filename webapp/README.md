**Api:**

To verify face: 
>localhost:5000/api_v3 (Method: POST, Json: {url: "your url"})
>> => Output {
    status,
    name,
    execute_time,
}

To create new face: 
>localhost:5000/api_v3/create (Method: POST, Json: {url: "your url", name: "your name"})
>> => Output {
    status
    execute_time
}

To scan face: 
>localhost:5000/api_v3/scan (Method: GET)
>> => Output {
    add
    exist
    total
    execute_time
}

To get list: 
>localhost:5000/api_v3/list (Method: GET)
>> => Output {
    *json list*
}

To rename face: 
>localhost:5000/api_v3/rename (Method: POST, Json: {oldname: "your oldname", newname: "your newname"})
>> => Output {
    status
    execute_time
}

To delete face: 
>localhost:5000/api_v3/delete (Method: POST, Json: {name: "your name"})
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
