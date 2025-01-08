package com.booking.spring.login.controllers;

import com.booking.spring.login.message.ResponseMessage;
import com.booking.spring.login.service.FileStorageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@CrossOrigin(origins = "http://localhost:8081", maxAge = 3600, allowCredentials="true")
@RestController
@RequestMapping("/api")
public class DepartmentImagesController {

    @Autowired
    private FileStorageService fss;

    @PostMapping("/{id}/upload")
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<ResponseMessage> uploadFile(@PathVariable("id") long id,
                                                      @RequestParam("file") MultipartFile file) {
        String message = "";
        try {
            fss.store(file, id);

            message = "Uploaded the file successfully: " + file.getOriginalFilename();
            return ResponseEntity.status(HttpStatus.OK).body(new ResponseMessage(message));
        } catch (Exception e) {
            System.out.println("E:"+ e.getMessage());
            message = "Could not upload the file: " + file.getOriginalFilename() + "!";
            return ResponseEntity.status(HttpStatus.EXPECTATION_FAILED).body(new ResponseMessage(message));
        }
    }
}
