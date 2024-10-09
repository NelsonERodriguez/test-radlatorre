import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class ApiService {
    private baseUrl = 'http://localhost:5000';
    constructor(private http: HttpClient) { }

    getRoles(): Observable<any> {
        return this.http.get(`${this.baseUrl}/roles`);
    }
    addRole(data: any): Observable<any> {
        return this.http.post(`${this.baseUrl}/roles`, data);
    }
    updateRole(id: number, data: any): Observable<any> {
        return this.http.put(`${this.baseUrl}/roles/${id}`, data);
    }

    getDepartments(): Observable<any> {
        return this.http.get(`${this.baseUrl}/departments`);
    }

    addDepartment(data: any): Observable<any> {
        return this.http.post(`${this.baseUrl}/departments`, data);
    }

    updateDepartment(id: number, data: any): Observable<any> {
        return this.http.put(`${this.baseUrl}/departments/${id}`, data);
    }

    getEmployees(): Observable<any> {
        return this.http.get(`${this.baseUrl}/employees`);
    }
    addEmployee(data: any): Observable<any> {
        return this.http.post(`${this.baseUrl}/employees`, data);
    }
    updateEmployee(id: number, data: any): Observable<any> {
        return this.http.put(`${this.baseUrl}/employees/${id}`, data);
    }
}