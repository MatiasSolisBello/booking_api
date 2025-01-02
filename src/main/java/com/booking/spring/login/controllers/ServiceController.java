package com.booking.spring.login.controllers;

import com.booking.spring.login.models.Service;
import com.booking.spring.login.repository.ServiceRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@CrossOrigin(origins = "http://localhost:8081", maxAge = 3600, allowCredentials="true")
@RestController
@RequestMapping("/api")
public class ServiceController {
    @Autowired
    private ServiceRepository serviceRepository;

    @PostMapping("/service")
    @PreAuthorize("hasRole('ADMIN')")
    public void saveService(@RequestBody Service ser) {
        serviceRepository.save(ser);
    }

    @GetMapping("/service")
    @PreAuthorize("hasRole('ADMIN')")
    public List<Service> getAllService(){
        return serviceRepository.findAll();
    }

    @GetMapping("/service/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public Optional<Service> getServiceById(@PathVariable("id") Long id) {
        return serviceRepository.findById(id);
    }
}
