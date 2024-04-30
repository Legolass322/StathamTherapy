import type {FC} from 'react'
import {memo} from 'react'

const ChatInner: FC = () => {
  return <div className="text-3xl font-bold underline text-center">Local</div>
}

export const Chat = memo(ChatInner)
