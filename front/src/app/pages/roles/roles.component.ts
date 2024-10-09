import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api.service';

@Component({
    selector: 'app-roles',
    templateUrl: './roles.component.html',
    styleUrls: ['./roles.component.css']
})
export class RolesComponent {
    roles: any[] = [];
    isModalOpen = false;
    isEditing = false;
    selectedRole: any = { name: '', active: true };

    constructor(private apiService: ApiService) {}

    ngOnInit() {
        this.loadRoles();
    }

    loadRoles() {
        this.apiService.getRoles().subscribe(data => {
        this.roles = data;
        });
    }

    openAddModal() {
        this.isModalOpen = true;
        this.isEditing = false;
        this.selectedRole = { name: '', active: true };
    }

    openEditModal(role: any) {
        this.isModalOpen = true;
        this.isEditing = true;
        this.selectedRole = { ...role };
    }

    closeModal() {
        this.isModalOpen = false;
    }

    addRole() {
        if (this.selectedRole.name) {
        this.apiService.addRole(this.selectedRole).subscribe(() => {
            this.loadRoles();
            this.closeModal();
        });
        }
    }

    updateRole() {
        if (this.selectedRole.name) {
        this.apiService.updateRole(this.selectedRole.id, this.selectedRole).subscribe(() => {
            this.loadRoles();
            this.closeModal();
        });
        }
    }
}
