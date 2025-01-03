package com.booking.spring.login.models;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

@Entity
public class Department {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotNull
    @Column
    private int price;

    @Enumerated(EnumType.STRING)
    @Column(length = 20)
    private EDepartmentStatus status;

    @NotNull
    @Size(max = 100)
    @Column
    private String city;

    @NotNull
    @Size(max = 100)
    @Column
    private String description;

    public Department() {
    }

    public Department(Long id, int price, EDepartmentStatus status, String city, String description) {
        this.id = id;
        this.price = price;
        this.status = status;
        this.city = city;
        this.description = description;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    @NotNull
    public int getPrice() {
        return price;
    }

    public void setPrice(@NotNull int price) {
        this.price = price;
    }

    public EDepartmentStatus getStatus() {
        return status;
    }

    public void setStatus(EDepartmentStatus status) {
        this.status = status;
    }

    public @NotNull @Size(max = 100) String getCity() {
        return city;
    }

    public void setCity(@NotNull @Size(max = 100) String city) {
        this.city = city;
    }

    public @NotNull @Size(max = 100) String getDescription() {
        return description;
    }

    public void setDescription(@NotNull @Size(max = 100) String description) {
        this.description = description;
    }
}
