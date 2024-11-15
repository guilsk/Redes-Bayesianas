import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
	providedIn: 'root'
})
export class ApiService {
	private apiUrl = 'http://localhost:8000'; // Altere para a URL onde sua API está rodando

	constructor(private http: HttpClient) { }

	public postData(data: any): Observable<any> {
		data = {
			'valor': 1600,
			'renda': 10000,
			'tempoEmpregado': 6,
			'taxaJuros': 14.74,
			'statusCalote': true,
			'caloteHistorico': false,
			'posseImoveis': 'OWN',
			'intencao': 'VENTURE'
		}
		return this.http.post(`${this.apiUrl}/VerificarCredito`, data);
	}

	// Adicione outros métodos de acordo com a sua API
}
