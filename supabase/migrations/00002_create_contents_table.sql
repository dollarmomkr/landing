-- Create contents table for products and stories
CREATE TABLE IF NOT EXISTS public.contents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    category TEXT NOT NULL CHECK (category IN ('product', 'story')),
    title TEXT NOT NULL,
    summary TEXT,
    content TEXT,
    image_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    owner_user_id UUID REFERENCES auth.users(id)
);

-- Enable RLS
ALTER TABLE public.contents ENABLE ROW LEVEL SECURITY;

-- Allow public to select
CREATE POLICY "Allow public to view contents"
    ON public.contents
    FOR SELECT
    TO public
    USING (true);

-- Allow authenticated users to insert contents
CREATE POLICY "Allow authenticated users to insert contents"
    ON public.contents
    FOR INSERT
    TO authenticated
    WITH CHECK (true);

-- Allow authenticated users to update their contents
CREATE POLICY "Allow authenticated users to update contents"
    ON public.contents
    FOR UPDATE
    TO authenticated
    USING (true);

-- Allow authenticated users to delete contents
CREATE POLICY "Allow authenticated users to delete contents"
    ON public.contents
    FOR DELETE
    TO authenticated
    USING (true);
