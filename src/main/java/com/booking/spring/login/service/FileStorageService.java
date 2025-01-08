package com.booking.spring.login.service;

import com.booking.spring.login.models.Department;
import com.booking.spring.login.models.DepartmentImages;
import com.booking.spring.login.repository.DepartmentImagesRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.Optional;

@Service
public class FileStorageService {
    @Autowired
    private DepartmentImagesRepository departmentImagesRepository;

    public DepartmentImages store(MultipartFile file, Long id) throws IOException {
        String fileName = StringUtils.cleanPath(file.getOriginalFilename());
        System.out.println("fileName: "+ fileName);
        System.out.println("file.getContentType(): "+ file.getContentType());
        System.out.println("file.getBytes(): "+ file.getBytes());

        DepartmentImages departImage = new DepartmentImages('', fileName, file.getContentType(),
                file.getBytes(), id);
        System.out.println("----------------------");

        return departmentImagesRepository.save(departImage);
    }
}
