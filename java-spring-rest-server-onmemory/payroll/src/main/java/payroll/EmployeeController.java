package payroll;

import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.*;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.hateoas.CollectionModel;
import org.springframework.hateoas.EntityModel;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
class EmployeeController {

	private final EmployeeRepository repository;

	EmployeeController(EmployeeRepository repository) {
		this.repository = repository;
	}

	@GetMapping("/employees")
	CollectionModel<EntityModel<Employee>> selectAllEmployee() {

		List<EntityModel<Employee>> employees = repository.findAll().stream()
				.map(employee -> EntityModel.of(employee,
						linkTo(methodOn(EmployeeController.class).selectEmployee(employee.getId())).withSelfRel(),
						linkTo(methodOn(EmployeeController.class).selectAllEmployee()).withRel("employees")))
				.collect(Collectors.toList());

		return CollectionModel.of(employees, linkTo(methodOn(EmployeeController.class).selectAllEmployee()).withSelfRel());
	}

	@GetMapping("/employees/{id}")
	EntityModel<Employee> selectEmployee(@PathVariable Long id) {

		Employee employee = repository.findById(id)
				.orElseThrow(() -> new EmployeeNotFoundException(id));

		return EntityModel.of(employee,
				linkTo(methodOn(EmployeeController.class).selectEmployee(id)).withSelfRel(),
				linkTo(methodOn(EmployeeController.class).selectAllEmployee()).withRel("employees"));
	}

	@PostMapping("/employees")
	Employee createEmployee(@RequestBody Employee newEmployee) {
		return repository.save(newEmployee);
	}


	@PutMapping("/employees/{id}")
	Employee updateEmployee(@RequestBody Employee newEmployee, @PathVariable Long id) {

		return repository.findById(id)
				.map(employee -> {
					employee.setName(newEmployee.getName());
					employee.setRole(newEmployee.getRole());
					return repository.save(employee);
				})
				.orElseGet(() -> {
					newEmployee.setId(id);
					return repository.save(newEmployee);
				});
	}

	@DeleteMapping("/employees/{id}")
	void deleteEmployee(@PathVariable Long id) {
		repository.deleteById(id);
	}
}
