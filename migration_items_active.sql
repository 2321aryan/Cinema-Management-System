-- Add active status specific column to items table
alter table public.items 
add column if not exists is_active boolean default true;
