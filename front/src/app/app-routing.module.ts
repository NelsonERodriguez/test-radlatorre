import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EmployeesComponent } from './pages/employees/employees.component';
import { RolesComponent } from './pages/roles/roles.component';
import { DepartmentsComponent } from './pages/departments/departments.component';

const routes: Routes = [
    { path: 'roles', component: RolesComponent },
    { path: 'departments', component: DepartmentsComponent },
    { path: 'employees', component: EmployeesComponent },
    { path: '', redirectTo: '/roles', pathMatch: 'full' }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }
