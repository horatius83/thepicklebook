import {LitElement, html} from 'https://cdn.skypack.dev/lit';

export class MaxInputSearch extends LitElement {
    static properties = {
        mxLabel: {type: String},
        mxName: {type: String},
        endpoint: {type: String},
        elements: {type: Array}
    };

    get listName() {
        return this.mxLabel + "_list";
    }

    constructor() {
        super();
        this.mxLabel = '';
        this.mxName = '';
        this.endpoint = '';
        this.elements = [];
        window.addEventListener('load', async (event) => {
            if (this.endpoint) {
                try {
                    const result = await fetch(this.endpoint, {
                        headers: {
                            'Accept': 'application/json',
                            'X-Requested-With': 'XMLHttpRequest'
                        }
                    });
                    this.elements = await result.json();
                } catch (e) {
                    console.error(e);
                }
            } else {
                console.error("mx-inputsearch : endpoint is not defined");
            }
        });
    }

    render() {
        return html`
            <link rel="stylesheet" href="/pickles/static/css/mini-css/3.0.1/mini-default.min.css" />
            <div class="input-group vertical">
                <label for="${this.mxName}">${this.mxLabel} </label>
                <input list="${this.listName}" name="${this.mxName}" id="${this.mxName}"></input>
            </div>
            <datalist id="${this.listName}">
                ${this.elements.map((e) => {
                    return html`<option value="${e}"></option>`
                })} 
            </datalist>
        `;
    }
}
customElements.define('mx-inputsearch', MaxInputSearch);