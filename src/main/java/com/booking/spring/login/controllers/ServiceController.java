package com.booking.spring.login.controllers;

import com.booking.spring.login.models.Service;
import com.booking.spring.login.repository.ServiceRepository;
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

    @DeleteMapping("/service/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<HttpStatus> deleteService(@PathVariable("id") Long id) {
        try {
            serviceRepository.deleteById(id);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PutMapping("/service/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<Service> updateService(@PathVariable("id") long id,
                                                 @RequestBody Service service) {
        Optional<Service> serviceData = serviceRepository.findById(id);
        //System.out.println("serviceData: " + serviceData);

        if (serviceData.isPresent()) {
            Service _service = serviceData.get();
            _service.setName(service.getName());
            _service.setDescription(service.getDescription());
            _service.setPrice(service.getPrice());
            return new ResponseEntity<>(serviceRepository.save(_service), HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
}
