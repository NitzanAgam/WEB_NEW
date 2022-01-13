console.log("im in fetch");

function get_users(){
    url = 'https://reqres.in/api/users'
    user_id = document.getElementById("user_id").value;
    if (user_id != ""){
        url = `https://reqres.in/api/users/${user_id}`;
    }

    fetch(url).then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data, user_id)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data, user_id){
    const curr_main = document.querySelector("main");

    for(let i = 0; i < curr_main.childElementCount, i++;){
        var child = curr_main.children[i];
        curr_main.removeChild(child);
    }

    if(user_id == "") {
        for(let user of response_obj_data){
            const section = document.createElement('section');
            section.innerHTML = `
            <img src="${user.avatar}" alt="Profile Picture"/> 
            <div>
                <span> ${user.first_name} ${user.last_name}</span>
                <br>
                <a href="mailto:${user.email}">Send Email</a>   
            </div>
            `;
            curr_main.appendChild(section);
        }
    } else {
        const section = document.createElement('section');
        section.innerHTML = `
        <img src="${response_obj_data.avatar}" alt="Profile Picture"/> 
        <div>
            <span> ${response_obj_data.first_name} ${response_obj_data.last_name}</span>
            <br>
            <a href="mailto:${response_obj_data.email}">Send Email</a>   
        </div>
        `;
        curr_main.appendChild(section);
    }
}