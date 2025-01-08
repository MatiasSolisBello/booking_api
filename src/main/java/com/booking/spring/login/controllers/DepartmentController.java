package com.booking.spring.login.controllers;

import com.booking.spring.login.models.Department;
import com.booking.spring.login.repository.DepartmentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@CrossOrigin(origins = "http://localhost:8081", maxAge = 3600, allowCredentials="true")
@RestController
@RequestMapping("/api")
public class DepartmentController {
    @Autowired
    private DepartmentRepository departmentRepository;

    @PostMapping("/department")
    @PreAuthorize("hasRole('ADMIN')")
    public void saveDepartment(@RequestBody Department department) {
        departmentRepository.save(department);
    }

    @GetMapping("/department")
    @PreAuthorize("hasRole('ADMIN')")
    public List<Department> getAllDepartment(){
        return departmentRepository.findAll();
    }

    @GetMapping("/department/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public Optional<Department> getDepartmentById(@PathVariable("id") Long id) {
        return departmentRepository.findById(id);
    }

    @DeleteMapping("/department/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<HttpStatus> deleteDepartment(@PathVariable("id") Long id) {
        try {
            departmentRepository.deleteById(id);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
