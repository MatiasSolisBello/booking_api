package com.booking.spring.login.models;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

@Entity
public class Service {
    @Id
    @GeneratedValue(strategy= GenerationType.IDENTITY)
    private Long id;

    @NotNull
    @Size(max = 100)
    @Column
    private String name;

    @NotNull
    @Size(max = 100)
    @Column
    private String description;

    @NotNull
    @Column
    private int price;

    public Service() {
    }

    public Service(int price, String description, String name, Long id) {
        this.price = price;
        this.description = description;
        this.name = name;
        this.id = id;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public @NotNull @Size(max = 100) String getName() {
        return name;
    }

    public void setName(@NotNull @Size(max = 100) String name) {
        this.name = name;
    }

    public @NotNull @Size(max = 100) String getDescription() {
        return description;
    }

    public void setDescription(@NotNull @Size(max = 100) String description) {
        this.description = description;
    }

    @NotNull
    public int getPrice() {
        return price;
    }

    public void setPrice(@NotNull int price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return "Service{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", description='" + description + '\'' +
                ", price=" + price +
                '}';
    }
}
