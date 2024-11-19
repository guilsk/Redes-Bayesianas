import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
	providedIn: 'root'
})
export class ApiService {
	private apiUrl = 'http://localhost:8000';

	constructor(private http: HttpClient) { }

	public postData(data: any): Observable<any> {
		return this.http.post(`${this.apiUrl}/VerificarCredito`, data);
	}
}
