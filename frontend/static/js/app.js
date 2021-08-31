buildList()

function buildList(){
    var url = 'http://127.0.0.1:8000/api/task-list';

    var listWrapper = document.getElementById('list-wrapper');

    fetch(url)
        .then((res) => res.json())
        .then((data) => {
            console.log(data);

            for (var i in data){

                var item = `
                <div id="data-row-${i}" class="task-wrapper flex-wrapper">
                    <div style="flex:7">
                        <span class="title">${data[i].title}</span>
                    </div>
                    <div style="flex:1">
                        <button class="btn btn-sm btn-outline-info edit">Edit </button>
                    </div>
                    <div style="flex:1">
                        <button class="btn btn-sm btn-outline-dark delete">-</button>
                    </div>
                </div>
                `;

                listWrapper.innerHTML += item;
            }        
        })

        var form = document.getElementById('form-wrapper');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            console('ok')
        })
}
