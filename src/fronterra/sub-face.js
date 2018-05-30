var demo = angular.module("grdp-demo", []);

demo.controller("bossman",

	function bossman($scope) {
		$scope.model = {
			contacts: [
				{ id: 	1, name: "Ana", mail:"mail@ana", phone:"", address:"", age:28 },
			],
			selected: {}
		};

		// gets the template to ng-include for a table row / item
		$scope.getTemplate = function (contact) {
			if (contact.id === $scope.model.selected.id) return 'edit';
			else return 'display';
		};

		$scope.editContact = function (contact) {
			$scope.model.selected = angular.copy(contact);
		};

		$scope.saveContact = function (idx) {
			console.log("Saving contact");
			$scope.model.contacts[idx] = angular.copy($scope.model.selected);
			$scope.reset();
		};

		$scope.reset = function () {
			$scope.model.selected = {};
		};
	}
);
