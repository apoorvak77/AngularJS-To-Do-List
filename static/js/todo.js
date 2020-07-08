var app = angular.module('toDo',[]);
app.controller('toDoController', function($scope, $http){
    //$scope.todoList = [{todoText:'Keep working on React'}];
    $http.get('/todo/api/').then(function(response){
        $scope.todoList=[];
        console.log(response.data)
        for(var i =0; i<response.data.length; i++){
            var todo = {};
            todo.todoText = response.data[i].todo_text;
            $scope.todoList.push(todo);
            console.log(todo)
        }
    })
    $scope.todoAdd = function(){
        $scope.todoList.push({todoText: $scope.todoInput});
        $scope.todoInput ='';
    }

    $scope.remove = function(){
        var oldList = $scope.todoList;
        $scope.todoList =[];
        angular.forEach(oldList, function(x){
            if(!x.done) $scope.todoList.push(x)
        })
    }

    $scope.saveData = function(){
        var data = {todo_text: $scope.todoInput}
        $http.put('/todo/api/',data)
    }
})