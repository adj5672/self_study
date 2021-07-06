# React 실습

> Tic Tac Toe



### 1. 초기 코드 설정

1. index.css

   ```css
   body {
     font: 14px "Century Gothic", Futura, sans-serif;
     margin: 20px;
   }
   
   ol, ul {
     padding-left: 30px;
   }
   
   .board-row:after {
     clear: both;
     content: "";
     display: table;
   }
   
   .status {
     margin-bottom: 10px;
   }
   
   .square {
     background: #fff;
     border: 1px solid #999;
     float: left;
     font-size: 24px;
     font-weight: bold;
     line-height: 34px;
     height: 34px;
     margin-right: -1px;
     margin-top: -1px;
     padding: 0;
     text-align: center;
     width: 34px;
   }
   
   .square:focus {
     outline: none;
   }
   
   .kbd-navigation .square:focus {
     background: #ddd;
   }
   
   .game {
     display: flex;
     flex-direction: row;
   }
   
   .game-info {
     margin-left: 20px;
   }
   
   ```

2. index.js

   ```react
   import React from 'react';
   import ReactDOM from 'react-dom';
   import './index.css';
   
   class Square extends React.Component {
     render() {
       return (
         <button className="square">
           {/* TODO */}
         </button>
       );
     }
   }
   
   class Board extends React.Component {
     renderSquare(i) {
       return <Square />;
     }
   
     render() {
       const status = 'Next player: X';
   
       return (
         <div>
           <div className="status">{status}</div>
           <div className="board-row">
             {this.renderSquare(0)}
             {this.renderSquare(1)}
             {this.renderSquare(2)}
           </div>
           <div className="board-row">
             {this.renderSquare(3)}
             {this.renderSquare(4)}
             {this.renderSquare(5)}
           </div>
           <div className="board-row">
             {this.renderSquare(6)}
             {this.renderSquare(7)}
             {this.renderSquare(8)}
           </div>
         </div>
       );
     }
   }
   
   class Game extends React.Component {
     render() {
       return (
         <div className="game">
           <div className="game-board">
             <Board />
           </div>
           <div className="game-info">
             <div>{/* status */}</div>
             <ol>{/* TODO */}</ol>
           </div>
         </div>
       );
     }
   }
   
   // ========================================
   
   ReactDOM.render(
     <Game />,
     document.getElementById('root')
   );
   ```

​	![image-20210703163348110](README.assets/image-20210703163348110.png)

- Square - `<button>` 렌더링
- Board - 사각형 9개 렌더링
- Game - 게임판 렌더링



### 2. Props를 통해 데이터 전달

> Board => Square 로 props 전달

1. Square에 value prop 전달

   ```react
   class Board extends React.Component {
     renderSquare(i) {
       return <Square value={i} />;
     }
   ```

2. 전달받은 value 값 표시

   ```react
   class Square extends React.Component {
     render() {
       return (
         <button className="square">
           {this.props.value}
         </button>
       );
     }
   }
   ```

   ![image-20210703164944794](README.assets/image-20210703164944794.png)



### 3. 사용자와 상호작용하는 컴포넌트 만들기

1. Square 클릭 시 X가 체크되도록 설정

   ```react
   class Square extends React.Component {
     render() {
       return (
         <button className="square" onClick={() => {
           alert('click')
         }}>
           {this.props.value}
         </button>
       );
     }
   }
   ```

   ![image-20210703165615568](README.assets/image-20210703165615568.png)

2. class에 생성자를 추가하여 state를 초기화

   ```react
   class Square extends React.Component {
     constructor(props) {
       super(props);
       this.state = {
         value: null,
       };
     }
   ```

   - **주의** 

     [JavaScript 클래스](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)에서 하위 클래스의 생성자를 정의할 때 항상 `super`를 호출해야합니다. 

     모든 React 컴포넌트 클래스는 `생성자`를 가질 때 `super(props)` 호출 구문부터 작성해야 합니다.

3. Square에 state 값을 표시

   ```react
    render() {
       return (
         <button 
           className="square" 
           onClick={() => {
             this.setState({value: 'X'})
           }}
         >
           {this.state.value}
         </button>
       );
     }
   ```

   ![image-20210703170532088](README.assets/image-20210703170532088.png)



### 4. State 끌어올리기

1. 부모 컴포넌트(Board)에 생성자 추가 및 9개의 null 배열을 초기 state로 설정

   ```react
   class Board extends React.Component {
     constructor(props) {
       super(props);
       this.state = {
         squares: Array(9).fill(null),
       };
     }
   ```

2. 각 Square에 props로 squares[i] 내려주기

   ```react
     renderSquare(i) {
       return <Square value={this.state.squares[i]} />;
     }
   ```

3. 클릭 시 Board에서 Square로 함수 전달

   ```react
     renderSquare(i) {
       return (
         <Square 
           value={this.state.squares[i]} 
           onClick={() => this.handleClick(i)}
         />
       );
     }
   ```

4. Square props 적용

   ```react
   class Square extends React.Component {
     render() {
       return (
         <button 
           className="square" 
           onClick={() => {
             this.props.onClick()
           }}
         >
           {this.props.value}
         </button>
       );
     }
   }
   ```

   - Square 클릭시 동작 과정
     1. 내장된 DOM `<button>` 컴포넌트에 있는 `onClick` prop은 React에게 클릭 이벤트 리스너를 설정하라고 알려줍니다.
     2. 버튼을 클릭하면 React는 Square의 `render()` 함수에 정의된 `onClick` 이벤트 핸들러를 호출합니다.
     3. 이벤트 핸들러는 `this.props.onClick()`를 호출합니다. Square의 `onClick` prop은 Board에서 정의되었습니다.
     4. Board에서 Square로 `onClick={() => this.handleClick(i)}`를 전달했기 때문에 Square를 클릭하면 `this.handleClick(i)`를 호출합니다.
     5. 아직 `handleClick()`를 정의하지 않았기 때문에 코드가 깨질 것입니다. 지금은 사각형을 클릭하면 “this.handleClick is not a function”과 같은 내용을 표시하는 붉은 에러 화면을 보게됩니다.

5. handleClick 정의

   ```react
     handleClick(i) {
       const squares = this.state.squares.slice()
       squares[i] = 'X'
       this.setState({squares: squares})
     }
   ```

   - .slice()를 사용하여 squares 배열의 사본 생성 (이유는 다음과 같다.)



### 5. 불변성이 중요한 이유

이전 코드 예시에서 기존 배열을 수정하는 것이 아니라 `.slice()` 연산자를 사용하여 `squares` 배열의 사본 만들기를 추천했습니다. 지금부터 불변성이 무엇인지와 왜 불변성이 중요한지 알아보겠습니다.

일반적으로 데이터 변경에는 두 가지 방법이 있습니다. 첫 번째는 데이터의 값을 직접 *변경*하는 것입니다. 두 번째는 원하는 변경 값을 가진 새로운 사본으로 데이터를 교체하는 것입니다.

#### 객체 변경을 통해 데이터 수정하기

```react
var player = {score: 1, name: 'Jeff'};
player.score = 2;
// 이제 player는 {score: 2, name: 'Jeff'}입니다.
```

#### 객체 변경 없이 데이터 수정하기

```react
var player = {score: 1, name: 'Jeff'};

var newPlayer = Object.assign({}, player, {score: 2});
// 이제 player는 변하지 않았지만 newPlayer는 {score: 2, name: 'Jeff'}입니다.

// 만약 객체 spread 구문을 사용한다면 이렇게 쓸 수 있습니다.
// var newPlayer = {...player, score: 2};
```

최종 결과는 동일하지만 직접적인 객체 변경이나 기본 데이터의 변경을 하지 않는다면 아래에 기술된 몇 가지 이점을 얻을 수 있습니다.

#### 복잡한 특징들을 단순하게 만듦

불변성은 복잡한 특징들을 구현하기 쉽게 만듭니다. 자습서에서는 “시간 여행” 기능을 구현하여 틱택토 게임의 이력을 확인하고 이전 동작으로 “되돌아갈 수 있습니다”. 이 기능은 게임에만 국한되지 않습니다. 특정 행동을 취소하고 다시 실행하는 기능은 애플리케이션에서 일반적인 요구사항 입니다. 직접적인 데이터 변이를 피하는 것은 이전 버전의 게임 이력을 유지하고 나중에 재사용할 수 있게 만듭니다.

#### 변화를 감지함

객체가 직접적으로 수정되기 때문에 복제가 가능한 객체에서 변화를 감지하는 것은 어렵습니다. 감지는 복제가 가능한 객체를 이전 사본과 비교하고 전체 객체 트리를 돌아야 합니다.

불변 객체에서 변화를 감지하는 것은 상당히 쉽습니다. 참조하고 있는 불변 객체가 이전 객체와 다르다면 객체는 변한 것입니다.

#### React에서 다시 렌더링하는 시기를 결정함

불변성의 가장 큰 장점은 React에서 *순수 컴포넌트*를 만드는 데 도움을 준다는 것입니다. 변하지 않는 데이터는 변경이 이루어졌는지 쉽게 판단할 수 있으며 이를 바탕으로 컴포넌트가 다시 렌더링할지를 결정할 수 있습니다.

`shouldComponentUpdate()`와 *순수 컴포넌트*를 작성하는 법에 대해 더 알아보고 싶다면 [성능 최적화하기](https://ko.reactjs.org/docs/optimizing-performance.html#examples)를 보세요.



### 6. 함수 컴포넌트

Square 컴포넌트를 함수 컴포넌트로 전환

```react
function Square(props) {
  return (
    <button className="square" onClick={props.onClick}>
      {props.value}
    </button>
  );
}
```



### 7. 순서 만들기

1. 첫 번째 차례를 "X"로 시작하기

   ```react
   class Board extends React.Component {
     constructor(props) {
       super(props);
       this.state = {
         squares: Array(9).fill(null),
         xIsNext: true,
       };
     }
   ```

2. 클릭할 때 마다 xIsNext 값 뒤집기 위해 handleClick 함수 수정

   ```react
     handleClick(i) {
       const squares = this.state.squares.slice()
       squares[i] = this.state.xIsNext ? 'X' : 'O'
       this.setState({
         squares: squares,
         xIsNext: !this.state.xIsNext,
       })
     }
   ```

3. 어느 플레이어가 다음 플레이어인지 나타내기

   ```react
     render() {
       const status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
   ```



### 8. 승자 결정하기

1. 승부가 날 때와 더 이상 둘 곳이 없을 때를 알려주기 위해 함수 작성

   ```react
   function calculateWinner(squares) {
     const lines = [
       [0, 1, 2],
       [3, 4, 5],
       [6, 7, 8],
       [0, 3, 6],
       [1, 4, 7],
       [2, 5, 8],
       [0, 4, 8],
       [2, 4, 6],
     ];
     for (let i = 0; i < lines.length; i++) {
       const [a, b, c] = lines[i];
       if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
         return squares[a];
       }
     }
     return null;
   }
   ```

2. 어떤 플레이어가 우승했는지 알리기 위하여 함수 호출

   ```react
     render() {
       const winner = calculateWinner(this.state.squares)
       let status
       if (winner) {
         status = 'Winner: ' + winner
       } else {
         status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O')
       }
   ```

3. 승자가 결정되거나 이미 채워진 Square라면 handleClick 함수 무시

   ```react
   handleClick(i) {
       const squares = this.state.squares.slice()
       if (calculateWinner(squares) || squares[i]) {
         return
       } 
       squares[i] = this.state.xIsNext ? 'X' : 'O'
       this.setState({
         squares: squares,
         xIsNext: !this.state.xIsNext,
       })
     }
   ```

   

### 9. 동작에 대한 기록 저장하기

1. history 배열에 과거 squares 배열 저장하기

   ```react
   // 예시
   
   history = [
     // 첫 동작이 발생하기 전
     {
       squares: [
         null, null, null,
         null, null, null,
         null, null, null,
       ]
     },
     // 첫 동작이 발생한 이후
     {
       squares: [
         null, null, null,
         null, 'X', null,
         null, null, null,
       ]
     },
     // 두 번째 동작이 발생한 이후
     {
       squares: [
         null, null, null,
         null, 'X', null,
         null, null, 'O',
       ]
     },
     // ...
   ]
   ```



### 10. 다시 State 끌어 올리기

1. Game 컴포넌트에 history state 설정 (Game 컴포넌트의 생성자 안에 초기 state 설정)

   ```react
   class Game extends React.Component {
     constructor(props) {
       super(props);
       this.state = {
         history: [{
           squares: Array(9).fill(null),
         }],
         xIsNext: true,
       };
     }
   ```

2. Game => Board로 squares와 onClick props 전달

   ```react
   // Board
   
     renderSquare(i) {
       return (
         <Square 
           value={this.props.squares[i]} 
           onClick={() => this.props.onClick(i)}
         />
       );
     }
   ```

3. Game의 render 함수를 가장 최근 기록을 사용하도록 업데이트

   ```react
   // Game
   
    render() {
       const history = this.state.history
       const current = history[history.length - 1]
       const winner = calculateWinner(current.squares)
       let status
       if (winner) {
         status = 'Winner: ' + winner
       } else {
         status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O')
       }
   
       return (
         <div className="game">
           <div className="game-board">
             <Board 
               squares={current.squares}
               onClick={(i) => this.handleClick(i)}
             />
           </div>
           <div className="game-info">
             <div>{status}</div>
   ```

4. Board render 함수 중복제거

   ```react
   // Board
   
     render() {
       return (
         <div>
           <div className="board-row">
           ...
   ```

5. handleClick 함수를 Game 컴포넌트로 이동 및 함수 수정

   ```reacts
     handleClick(i) {
       const history = this.state.history
       const current = history[history.length - 1]
       const squares = current.squares.slice()
       if (calculateWinner(squares) || squares[i]) {
         return
       } 
       squares[i] = this.state.xIsNext ? 'X' : 'O'
       this.setState({
         history: history.concat([{
           squares: squares,
         }]),
         xIsNext: !this.state.xIsNext,
       })
     }
   ```

   - 배열 `push()` 함수와 같이 더 익숙한 방식과 달리 `concat()` 함수는 기존 배열을 변경하지 않기 때문에 이를 더 권장합니다.



### 11. 과거의 이동 표시하기

1. history mapping

   ```react
   render() {
       const history = this.state.history
       const current = history[history.length - 1]
       const winner = calculateWinner(current.squares)
   
       const moves = history.map((step, move) => {
         const desc = move ?
           'Go to move #' + move :
           'Go to game state'
         return (
           <li>
             <button onClick={() => this.jumpTo(move)}>{desc}</button>
           </li>
         )
       })
   
       let status
       if (winner) {
         status = 'Winner: ' + winner
       } else {
         status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O')
       }
   
       return (
         <div className="game">
           <div className="game-board">
             <Board 
               squares={current.squares}
               onClick={(i) => this.handleClick(i)}
             />
           </div>
           <div className="game-info">
             <div>{status}</div>
             <ol>{moves}</ol>
           </div>
         </div>
       );
     }
   ```

   - **경고 배열이나 이터레이터의 자식들은 고유의 “key” prop을 가지고 있어야 합니다. “Game”의 render 함수를 확인해주세요.**



### 12. Key 선택하기

리스트를 렌더링할 때 React는 렌더링하는 리스트 아이템에 대한 정보를 저장합니다. 리스트를 업데이트 할 때 React는 무엇이 변했는 지 결정해야 합니다. 리스트의 아이템들은 추가, 제거, 재배열, 업데이트 될 수 있습니다.

아래의 코드가

```html
<li>Alexa: 7 tasks left</li>
<li>Ben: 5 tasks left</li>
```

다음과 같이 변한다고 상상해 봅시다.

```html
<li>Ben: 9 tasks left</li>
<li>Claudia: 8 tasks left</li>
<li>Alexa: 5 tasks left</li>
```

사람의 눈에는 task 개수가 업데이트되었을 뿐만 아니라 Alexa와 Ben의 순서가 바뀌고 Claudia가 두 사람 사이에 추가되었다고 생각할 것입니다. 그러나 React는 컴퓨터 프로그램이며 사람이 의도한 바가 무엇인지 알지 못합니다. 그렇기 때문에 리스트 아이템에 *key* prop을 지정하여 각 아이템이 다른 아이템들과 다르다는 것을 알려주어야 합니다. 키를 지정하는 한 가지 방법은 `alexa`, `ben`, `claudia` 문자를 사용하는 것입니다. 만약 데이터베이스에서 데이터를 불러와서 표시한다면 Alexa, Ben, Claudia의 데이터베이스 ID가 키로 사용될 수 있습니다.

```html
<li key={user.id}>{user.name}: {user.taskCount} tasks left</li>
```

목록을 다시 렌더링하면 React는 각 리스트 아이템의 키를 가져가며 이전 리스트 아이템에서 일치하는 키를 탐색합니다. 현재 리스트에서 이전에 존재하지 않는 키를 가지고 있다면 React는 새로운 컴포넌트를 생성합니다. 현재 리스트가 이전 리스트에 존재했던 키를 가지고 있지 않다면 React는 그 키를 가진 컴포넌트를 제거합니다. 만약 두 키가 일치한다면 해당 구성요소는 이동합니다. 키는 각 컴포넌트를 구별할 수 있도록 하여 React에게 다시 렌더링할 때 state를 유지할 수 있게 합니다. 만약 컴포넌트의 키가 변한다면 컴포넌트는 제거되고 새로운 state와 함께 다시 생성됩니다.

React에서 `key`는 심화 기능인 `ref`와 동일하게 특별하고 미리 지정된 prop입니다. 엘리먼트가 생성되면 React는 `key` 속성을 추출하여 반환되는 엘리먼트에 직접 키를 저장합니다. `key`가 `props`에 속하는 것처럼 보이지만 `this.props.key`로 참조할 수 없습니다. React는 자동으로 `key`를 어떤 컴포넌트를 업데이트 할 지 판단하는 데에 사용합니다. 컴포넌트는 `key`를 조회할 수 없습니다.

**동적인 리스트를 만들 때마다 적절한 키를 할당할 것을 강력하게 추천합니다.** 적절한 키가 없는 경우 데이터 재구성을 고려해 볼 수 있습니다.

키가 지정되지 않은 경우 React는 경고를 표시하며 배열의 인덱스를 기본 키로 사용합니다. 배열의 인덱스를 키로 사용하는 것은 리스트 아이템 순서를 바꾸거나 아이템을 추가/제거 할 때 문제가 됩니다. 명시적으로 `key={i}`를 전달하면 경고가 나타나지는 않지만 동일한 문제를 일으키기 때문에 대부분의 경우에 추천하지 않습니다.

키는 전역에서 고유할 필요는 없으며 컴포넌트와 관련 아이템 사이에서는 고유한 값을 가져야 합니다.

### 

### 13. 시간 여행 구현하기

1. key 값 설정하기

   ```react
       const moves = history.map((step, move) => {
         const desc = move ?
           'Go to move #' + move :
           'Go to game state'
         return (
           <li key={move}>
             <button onClick={() => this.jumpTo(move)}>{desc}</button>
           </li>
         )
       })
   ```

2. state에 stepNumber 설정

   ```react
   class Game extends React.Component {
     constructor(props) {
       super(props);
       this.state = {
         history: [{
           squares: Array(9).fill(null),
         }],
         stepNumber: 0,
         xIsNext: true,
       };
     }
   ```

3. jumpTo 함수 정의

   ```react
     jumpTo(step) {
       this.setState({
         stepNumber: step,
         xIsNext: (step % 2) === 0,
       })
     }
   ```

4. handleClick의 history, stepNumber 수정

   ```react
     handleClick(i) {
       const history = this.state.history.slice(0, this.state.stepNumber + 1)
       const current = history[history.length - 1]
       const squares = current.squares.slice()
       if (calculateWinner(squares) || squares[i]) {
         return
       } 
       squares[i] = this.state.xIsNext ? 'X' : 'O'
       this.setState({
         history: history.concat([{
           squares: squares,
         }]),
         stepNumber: history.length,
         xIsNext: !this.state.xIsNext,
       })
     }
   ```

5. stepNumber에 맞는 현재 선택된 이동을 렌더링

   ```react
     render() {
       const history = this.state.history
       const current = history[this.state.stepNumber]
       const winner = calculateWinner(current.squares)
   ```

   

### 14. 마무리

축하합니다! 당신은 아래 기능을 가진 틱택토 게임을 만들었습니다.

- 틱택토를 할 수 있게 해주고,
- 게임에서 승리했을 때를 알려주며,
- 게임이 진행됨에 따라 게임 기록을 저장하고,
- 플레이어가 게임 기록을 확인하고 게임판의 이전 버전을 볼 수 있도록 허용합니다.

수고하셨습니다! 이제 React가 어떻게 동작하는지 이해하셨길 바랍니다.

최종 결과는 여기서 확인해주세요: **[최종 결과](https://codepen.io/gaearon/pen/gWWZgR?editors=0010)**.

시간이 더 있거나 새로운 React 기술을 연습하고 싶은 경우 다음과 같이 난이도를 높일 수 있는 틱택토 게임 개선 아이디어를 구현해보세요.

1. 이동 기록 목록에서 특정 형식(행, 열)으로 각 이동의 위치를 표시해주세요.
2. 이동 목록에서 현재 선택된 아이템을 굵게 표시해주세요.
3. 사각형들을 만들 때 하드코딩 대신에 두 개의 반복문을 사용하도록 Board를 다시 작성해주세요.
4. 오름차순이나 내림차순으로 이동을 정렬하도록 토글 버튼을 추가해주세요.
5. 승자가 정해지면 승부의 원인이 된 세 개의 사각형을 강조해주세요.
6. 승자가 없는 경우 무승부라는 메시지를 표시해주세요.

자습서를 통해 엘리먼트, 컴포넌트, props, state를 포함한 React의 개념을 다루었습니다. 각 항목에 대한 자세한 설명은 [문서의 다른 부분](https://ko.reactjs.org/docs/hello-world.html)을 참조하시길 바랍니다. 컴포넌트의 정의에 대한 자세한 내용은 [`React.Component` API 참조](https://ko.reactjs.org/docs/react-component.html)를 확인해주세요.

