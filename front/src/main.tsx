import {StrictMode} from 'react'
import {createRoot} from 'react-dom/client'
import {BrowserRouter} from 'react-router-dom'

import {App} from './components/App'

import './index.css'

function init(element: HTMLElement) {
  console.log('init', element)

  createRoot(element!).render(
    <StrictMode>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </StrictMode>,
  )
}

function waitForRoot(tries = 0, maxRetries = 10): Promise<HTMLElement> {
  console.log('wait')
  const p = new Promise<HTMLElement>((resolve, reject) => {
    const inner = () => {
      console.log('inner', tries)
      const element = document.getElementById('root')

      if (tries >= maxRetries) {
        reject('No root')
        return
      }

      if (!element) {
        setTimeout(() => {
          tries += 1
          inner()
        }, 100)
        return
      }

      resolve(element)
    }

    inner()
  })

  return p
}

// todo: find better fix
setTimeout(() => {
  waitForRoot()
    .then(v => init(v))
    .catch(v => console.log("Couldn't wait", v))
}, 1000)

// todo: remove
document.addEventListener('load', () => {
  console.log('document load')
})

document.addEventListener('DOMContentLoad', () => {
  console.log('document DOMContentLoad')
})
