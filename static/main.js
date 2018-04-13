var app = angular.module('mandi', []);
app.config([
    '$interpolateProvider',
    function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    }
]);
app.controller('myCtrl', function($scope, $http) {
	$scope.price = 0

    $http({
            method : "GET",
            url : "/get_names/cereal"
        }).then(function mySuccess(response) {
            $scope.cereals = response.data.cereals;
        }, function myError(response) {
            $scope.myWelcome = response.statusText;
        });
    $http({
            method : "GET",
            url : "/get_names/mandi"
        }).then(function mySuccess(response) {
            $scope.mandis = response.data.mandis;
        }, function myError(response) {
            $scope.myWelcome = response.statusText;
        });

    $scope.myFunc = function(){
    	if($scope.cereal_name == '' || $scope.cereal_name == undefined){
    		$scope.cereal_name = null
    	}

    	if($scope.mandi_name == '' || $scope.mandi_name == undefined){
    		$scope.mandi_name = null
    	}
    	if($scope.date1 == '' || $scope.date1 == undefined){
    		$scope.date1 = null
    	}
    	if($scope.date2 == '' || $scope.date2 == undefined){
    		$scope.date2 = null
    	}
    	q_data = {
    		"cereal":$scope.cereal_name,
    		"mandi" : $scope.mandi_name,
    		"date1": $scope.date1,
    		"date2": $scope.date2
    	}

    	$http({
    	        method : "POST",
    	        url : "/get_price",
    	        data: q_data,
    	    }).then(function mySuccess(response) {
    	        $scope.price_data = response.data.price_data;
    	        if ($scope.date1 == null || $scope.date2 == null){
    	        	$scope.only_price = true
    	        	$scope.price = $scope.price_data[0].modal_price
    	        }
    	        else{
    	        	var ctx = document.getElementById('myChart').getContext('2d');
    	        	var labels = []
    	        	var _data = []
    	        	$scope.show_chart = true
    	        	for (i in $scope.price_data){
    	        		labels.push(i)
    	        		console.log($scope.price_data[i][0])
    	        		_data.push($scope.price_data[i][0].modal_price)

    	        	}
    	        	console.log(_data)

    	        	var chart = new Chart(ctx,{
    	        		type: 'line',
    	        		data: {
        		        labels: labels,
        		        datasets: [{
        		            label: "Modal price",
        		            backgroundColor: 'rgb(255, 99, 132)',
        		            borderColor: 'rgb(255, 99, 132)',
        		            data: _data,
        		        	}]
    	        		},

    	        		    // Configuration options go here
    	        		options: {}
    	        	});

    	        	}
    	        },function myError(response) {
    	        	$scope.myWelcome = response.data
    	        	alert($scope.myWelcome)
    	        }); 
    }

});