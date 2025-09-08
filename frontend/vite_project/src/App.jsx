// App.jsx
import './App.scss'
import { Button } from 'antd';
function App() {
  return (
    <div className="wrapper">
      <header>

        <div className="headerLeft">
          <img src="/img/school_icon.svg" alt="schoolIcon" />
          <div>
            <Button type="default">Оставить отзыв</Button>
            <Button type="default">Отзывы</Button>
            <Button type="default">Преподаватели</Button>
          </div>

        </div>
        <div className="headerRight">
          <img  className="loginIcon" src="/img/login_icon.svg" alt="loginlIcon" />
          <Button type="default">Вход</Button>
          <Button type="default">Регистрация</Button>
        </div>
      </header>

      <div className="content">
        <h1>Последние отзывы</h1>
        <div className="lastReviews"></div>
        <ul>
          <li>
            <p>Отзыв 1</p>
            <p>Отзыв 2</p>
            <p>Отзыв 3</p>
          </li>
        </ul>
      </div>
    </div>
  )
}

export default App