# Design System

## Visual Direction

[One-sentence summary of the aesthetic — e.g., "Dark-mode developer tool with high information density and minimal chrome."]

## Color Palette

| Role | Hex | Usage |
|------|-----|-------|
| Background | `#XXXXXX` | Page background |
| Surface | `#XXXXXX` | Cards, panels, elevated surfaces |
| Primary | `#XXXXXX` | Primary actions, brand accent |
| Secondary | `#XXXXXX` | Secondary actions, muted elements |
| Text Primary | `#XXXXXX` | Body text, headings |
| Text Secondary | `#XXXXXX` | Captions, metadata, muted text |
| Border | `#XXXXXX` | Dividers, input borders |
| Error | `#XXXXXX` | Error states, destructive actions |
| Warning | `#XXXXXX` | Warning states |
| Success | `#XXXXXX` | Success states, confirmations |

## Typography

### Font Family
- UI text: [e.g., system font stack, Inter, SF Pro]
- Code / monospace: [e.g., JetBrains Mono, Fira Code, system monospace]

### Scale
- Heading 1: [size / weight / line-height]
- Heading 2: [size / weight / line-height]
- Heading 3: [size / weight / line-height]
- Body: [size / weight / line-height]
- Caption: [size / weight / line-height]

## Information Density

[Spacious (fewer elements, more whitespace), Dense (data-rich, compact), or Balanced.]

## Component Library

- Strategy: [e.g., Tailwind CSS + Radix UI, raw CSS, shadcn/ui, Material UI]
- Icon set: [e.g., Lucide, Heroicons, Phosphor, custom]

## Interaction Paradigms

### Loading States
- [e.g., Skeleton screens for page loads, spinners for button actions, optimistic UI for mutations]

### Transitions
- [e.g., Minimal — instant state changes, or subtle 150ms fades]

### Error States
- [e.g., Inline validation on forms, toast notifications for async errors, empty states with CTAs]

### Responsive Behavior
- Breakpoints: [e.g., mobile < 640px, tablet 640-1024px, desktop > 1024px]
- Strategy: [e.g., mobile-first, desktop-first, adaptive]

## Accessibility Requirements

- [e.g., WCAG 2.1 AA minimum, keyboard navigation, screen reader support, focus indicators]
- [e.g., Color contrast ratios: 4.5:1 for text, 3:1 for large text]

## Anti-Patterns (Do Not Use)

- [e.g., No bright white backgrounds in dark mode]
- [e.g., No pure black text on pure white backgrounds]
- [e.g., No animations longer than 300ms]
