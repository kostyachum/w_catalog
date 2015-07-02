var productsApp = angular.module('productsApp');

// productsApp.config(function ($stateProvider, $urlRouterProvider, RestangularProvider) {
// 	// For any unmatched url, send to /route1
// 	$urlRouterProvider.otherwise("/");
// 	$stateProvider
// 		.state('index', {

// 			url: "/main/",
// 			templateUrl: "catalog/index.html",
// 			controller: "ProductList"
// 		})

// 		// .state('new', {

// 		// 	url: "/new",
// 		// 	templateUrl: "/jobs/job-form",
// 		// 	controller: "JobFormCtrl"
// 		// })
// })


productsApp.controller 'AppController', ['$scope', '$http', ($scope, $http) ->
    $scope.posts = [
        author:
            username: 'Joe'
        title: 'Sample Post #1'
        body: 'This is the first sample post'
    ,
        author:
            username: 'Karen'
        title: 'Sample Post #2'
        body: 'This is another sample post'
    ]
]