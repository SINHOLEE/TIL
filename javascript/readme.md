# javascript 뻘짓



 

자바스크립트 오브젝트를 다루는 기초적인 부분

```javascript
console.log("----------ob1------")
console.log(ob1);
console.log(ob1.a);
console.log(ob1["a"]);
console.log("----------ob2------")
console.log(ob2);
console.log(ob2.a);
console.log(ob2["a"]);

```

다음과 같이 실행했을때 콘솔값은 아래와 같다.

```javascript
----------ob1------
{ a: 1, b: 2 }
1
1
----------ob2------
{"a": 1, "b":2}
undefined
undefined
```



아직 ob1과 ob2를 보여주지 않아 얼핏보면 왜 같은 객체형태인데 ob2는 undefined가 나오는지 영문을 모를것이다. 두 객체는 다음과 같다.

```javascript
let ob1 = {"a": 1, "b":2}
let ob2 = '{"a": 1, "b":2}'

```

하나는 오브젝트, 하나는 스트링 형식이다. 외부 라이브러니나, sdk를 불러와 쓰다보면 종종 이런경우를 자주 접하게 된다. 예를들어 하이퍼 페브릭 레저 SDK를 사용하다보면 페브릭 서버에서 state를 불러오는 경우가 있는데, 불러오는 객체가 스트링 값이다.

```javas
let asset = stub.getStates(Key);

console.log(asset);
---------console---------
{ a: 1, b: 2 }

if (asset.recorder === "recorder"){
	해당로직
}
```

이런식으로 나오는데,  asset.recorder로 접근하면 undefined 문제가 발생했었다. 그 이유가 바로 스트링으로반환되기 때문인데, 문제는 아래와 같이 변환하면 해결이 안된다는 것이다.



```javascript
let asset = stub.getStates(Key);

asset = JSON.parse(asset);
if (asset.recorder === "recorder"){
	해당로직
}
```

분명 형변환을 통해 object화 했지만 접근 불가능 했다. 다음과 같이 하면서 문제를 해결했다.



```javascript
let asset = stub.getStates(Key);

let asset1 = JSON.parse(asset);
if (asset1.recorder === "recorder"){
	해당로직
}
```

차이를 알겠는가? 새로운 객체를 다시 선언해야 그 선언된 객체로부터 .key값으로 접근할 수 있게 되는것이다. 

다른방식의 해결방법을 찾아보아야 겠다.

