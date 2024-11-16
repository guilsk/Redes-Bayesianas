import { Component } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { ApiService } from './shared/api.service';

@Component({
	selector: 'app-home',
	templateUrl: './home.component.html',
	styleUrls: ['./home.component.scss']
})
export class HomeComponent {
	form: FormGroup;
	result: boolean | null = null;
	hasError: boolean = false;

	constructor(private formBuilder: FormBuilder, private apiService: ApiService) {
		// Inicializa o formulário usando FormBuilder
		this.form = this.formBuilder.group({
			valor: [''],
			renda: [''],
			tempoEmpregado: [''],
			taxaJuros: [''],
			statusCalote: [false],
			caloteHistorico: [false],
			posseImoveis: ['OWN'],
			intencao: ['EDUCATION']
		});
	}

	postData(): void {
		if (this.form.valid) {
			const dataToSend = this.form.value;

			this.apiService.postData(dataToSend).subscribe({
				next: (response: boolean) => {
					this.result = response;
					this.hasError = false;
				},
				error: () => {
					this.hasError = true;
					this.result = null;
				}
			});
		} else {
			this.hasError = true;
			this.result = null;
		}
	}
}
