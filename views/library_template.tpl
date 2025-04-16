<div class="library">
    <div class="row">
        <label class="h1 text-center">Now Showing</label>            
    </div>
    <div class="row">
        <ul class="list-group">            
            %for movie in library:          
            <li class="list-group-item">
                <a class="btn btn-outline-primary" href="/video/{{movie}}" role="button">
                    {{movie}}
                </a>
            </li>
            %end
        </ul>
    </div>
<div>