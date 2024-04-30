import type {FC} from 'react'
import {Route, Routes} from 'react-router-dom'

import {Chat} from './Chat'
import {Profile} from './Profile'

export const AppRoutes: FC = () => {
  return (
    <div className="flex-grow">
      <Routes>
        <Route path="/profile/*" element={<Profile />} />
        <Route path="/chat/*" element={<Chat />} />
      </Routes>
    </div>
  )
}
