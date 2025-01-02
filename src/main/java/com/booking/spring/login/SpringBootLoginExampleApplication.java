package com.booking.spring.login;

import com.booking.spring.login.models.ERole;
import com.booking.spring.login.models.Role;
import com.booking.spring.login.repository.RoleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.annotation.Bean;
import org.springframework.context.event.EventListener;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@SpringBootApplication
public class SpringBootLoginExampleApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringBootLoginExampleApplication.class, args);
	}

	@Bean
	public WebMvcConfigurer corsConfigurer() {
		return new WebMvcConfigurer() {
			@Override
			public void addCorsMappings(CorsRegistry registry) {
				registry.addMapping("/**")
						.allowedOrigins("http://localhost:4200")
						.allowedMethods("*")
						.allowedHeaders("*");
			}
		};
	}

	@Autowired
	private RoleRepository roleRepository;

	@EventListener(ApplicationReadyEvent.class)
	public void initializeRoles() {
		for (ERole role : ERole.values()) {
			if (roleRepository.findByName(role).isEmpty()) {
				Role newRole = new Role();
				newRole.setName(role);
				roleRepository.save(newRole);
				System.out.println("Role " + role + " created.");
			}
		}
	}

}
