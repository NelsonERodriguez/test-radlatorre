import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
    selector: 'app-employees',
    templateUrl: './employees.component.html'
})
export class EmployeesComponent implements OnInit {
    employees: any[] = [];

    constructor(private apiService: ApiService) { }

    ngOnInit() {
        this.loadEmployees();
    }

    loadEmployees() {
        this.apiService.getEmployees().subscribe(data => {
        this.employees = data;
        });
    }

    addEmployee(employee: any) {
        this.apiService.addEmployee(employee).subscribe(() => {
        this.loadEmployees();
        });
    }

    updateEmployee(id: number, employee: any) {
        this.apiService.updateEmployee(id, employee).subscribe(() => {
        this.loadEmployees();
        });
    }
}
