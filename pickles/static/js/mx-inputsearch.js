import {LitElement, css, html} from 'https://cdn.skypack.dev/lit';

export class MaxInputSearch extends LitElement {
    static properties = {
        mxLabel: {type: String},
        mxName: {type: String},
        endpoint: {type: String},
        elements: {type: Array}
    };
    static styles = css`
        .input-group.vertical {
            display: flex;
            align-items: stretch;
            flex-direction: column;
        } 
    `;

    constructor() {
        super();
        this.mxLabel = '';
        this.mxName = '';
        this.endpoint = '';
        this.elements = [];
        window.addEventListener('load', (event) => {
            if (this.endpoint) {
                fetch(this.endpoint, {
                    headers: {
                        'Accept': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                .then(response => response.json())
                .then(pickleMakers => {
                    this.elements = pickleMakers;
                })
                .catch(err => console.error(err));
            } else {
                console.error("mx-inputsearch : endpoint is not defined");
            }
        });
    }

    getListName() {
        return this.mxLabel + "_list";
    }

    render() {
        return html`
            <div class="input-group vertical">
                <label for="${this.mxName}">${this.mxLabel} </label>
                <input list="${this.getListName()}" name="${this.mxName}" id="${this.mxName}"></input>
            </div>
            <datalist id="${this.getListName()}">
                ${this.elements.map((e) => {
                    return html`<option value="${e}"></option>`
                })} 
            </datalist>
        `;
    }
}
customElements.define('mx-inputsearch', MaxInputSearch);