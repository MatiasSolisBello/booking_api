import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Service } from '../models/service.model';

@Injectable({
  providedIn: 'root'
})
export class ServiceService {
  myAppUrl = 'http://localhost:8080/api';
	myApiUrl = '/service/';
  

	httpOptions = {
		headers: new HttpHeaders({
			'Content-Type': 'application/json',
    })
  };
  constructor(private http: HttpClient) { }

  getListServicio(): Observable<Service[]>{
    console.log('getListServicio: ', this.http.get<Service[]>(this.myAppUrl + this.myApiUrl));
    return this.http.get<Service[]>(this.myAppUrl + this.myApiUrl);
  }
}
