package payroll;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@Controller
@RequestMapping(path="/api")
class EmployeeController {

	@Autowired
	private EmployeeRepository repository;

	@GetMapping(path="/all")
	public @ResponseBody Iterable<Employee> selectAllEmployees(){
		return repository.findAll();
	}

	@GetMapping("/employees/{id}")
	public ResponseEntity<Employee> selectEmployeeById (@PathVariable Long id) {

		Optional<Employee> tobeSelectEmployee = repository.findById(id);

		if(tobeSelectEmployee.isPresent()){
			return new ResponseEntity<>(tobeSelectEmployee.get(),HttpStatus.OK);
		}else{
			return new ResponseEntity<>(tobeSelectEmployee.orElse(null), HttpStatus.NOT_FOUND);
		}

	}

	@PostMapping("/add")
	public ResponseEntity<Employee> createEmployee(@RequestBody Employee tobeCreateEmployee){

		repository.save(tobeCreateEmployee);

		return new ResponseEntity<>(tobeCreateEmployee, HttpStatus.OK);
	}


	@PutMapping("/employees/{id}")
	public ResponseEntity<Employee> updateEmployee(@RequestBody Employee newEmployee, @PathVariable Long id) throws EmployeeNotFoundException{

		Employee employee = repository.findById(id).orElseThrow(()->new EmployeeNotFoundException(id));

		employee.setName(newEmployee.getName());
		employee.setRole(newEmployee.getRole());

		Employee updatedEmployee = repository.save(employee);

		return new ResponseEntity<>(updatedEmployee, HttpStatus.OK);
	}

	@DeleteMapping("/employees/{id}")
	public ResponseEntity<Employee> deleteEmployee(@PathVariable Long id) throws EmployeeNotFoundException{

		Employee tobeDeleteEmployee = repository.findById(id).orElseThrow(()->new EmployeeNotFoundException(id));

		repository.delete(tobeDeleteEmployee);

		return new ResponseEntity<>(tobeDeleteEmployee,HttpStatus.OK);
	}
}
