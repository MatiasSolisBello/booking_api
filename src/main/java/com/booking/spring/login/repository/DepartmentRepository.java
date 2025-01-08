package com.booking.spring.login.repository;

import com.booking.spring.login.models.Department;
import com.booking.spring.login.models.EDepartmentStatus;
import com.booking.spring.login.models.ERole;
import com.booking.spring.login.models.Role;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface DepartmentRepository extends JpaRepository<Department, Long> {
    //Optional<T> findById(ID id);
}
