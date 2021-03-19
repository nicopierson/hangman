let dict2 = {
    name: {nested: "Ben", mail: "testmail"},
    age: 21,
    job: "Software Engineer Intern"
};

class Test{
    constructor() {
        this._dict = dict2;
    };

    get dict() {
        return this._dict;
    }

};

let test = new Test();
console.log(test.dict.name.nested);