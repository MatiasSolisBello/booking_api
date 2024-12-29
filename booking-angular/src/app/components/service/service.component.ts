import { Component, OnInit } from '@angular/core';
import { Service } from '../../models/service.model';
import { ServiceService } from '../../services/service.service';

@Component({
  selector: 'app-service',
  templateUrl: './service.component.html',
  styleUrl: './service.component.css'
})
export class ServiceComponent implements OnInit {
  listServicio?: Service[];
  constructor(private servicioService: ServiceService) { }

  ngOnInit(): void {
    this.cargarServicio();
  }

  cargarServicio(){
    this.servicioService.getListServicio().subscribe(data => {
      console.log('DATA: ', data);
      this.listServicio = data;
    });
  }
}
