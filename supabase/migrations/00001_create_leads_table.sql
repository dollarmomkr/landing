-- Create leads table for DollarMom MVP
CREATE TABLE IF NOT EXISTS public.leads (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    channel TEXT DEFAULT 'web',
    interest_category TEXT,
    memo TEXT,
    status TEXT DEFAULT 'new',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    owner_user_id UUID REFERENCES auth.users(id)
);

-- Enable RLS
ALTER TABLE public.leads ENABLE ROW LEVEL SECURITY;

-- Allow authenticated users (admin) to view all leads
CREATE POLICY "Allow authenticated users to view all leads"
    ON public.leads
    FOR SELECT
    TO authenticated
    USING (true);

-- Allow anyone to insert leads (public form submission)
CREATE POLICY "Allow public to insert leads"
    ON public.leads
    FOR INSERT
    TO public
    WITH CHECK (true);

-- Allow authenticated users to update leads
CREATE POLICY "Allow authenticated users to update leads"
    ON public.leads
    FOR UPDATE
    TO authenticated
    USING (true);

-- Allow authenticated users to delete leads
CREATE POLICY "Allow authenticated users to delete leads"
    ON public.leads
    FOR DELETE
    TO authenticated
    USING (true);
