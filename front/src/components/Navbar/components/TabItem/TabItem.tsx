import type {FC, ReactNode} from 'react'
import {memo} from 'react'

export type TabItemProps = {
  onClick: () => void
  text: ReactNode
  icon?: ReactNode
  active: boolean
}

const TabItemInner: FC<TabItemProps> = props => {
  const {onClick, text, icon, active} = props

  return (
    <button
      type="button"
      onClick={() => {
        if (!active) {
          onClick()
        }
      }}
    >
      {icon}
      <div>{text}</div>
    </button>
  )
}

export const TabItem = memo(TabItemInner)
